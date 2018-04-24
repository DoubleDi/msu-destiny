# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import logging
import os
import sys
import urllib

reload(sys)
sys.setdefaultencoding('utf8')

from PIL import Image

from destiny.models import Author, DestinyObject, ObjectType, PhotoItem, Place
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.mail import send_mail
from django.db.models import Prefetch, Q
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from msu_destiny.settings import BASE_DIR, MEDIA_ROOT, STATIC_ROOT
from random import randint

logger = logging.getLogger('django')


def auth_page(request):
    if request.method == 'GET':
        params = {}
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
            # return render(request, 'auth.html', params)
        else:
            return render(request, 'auth.html', params)


@login_required(login_url='/auth')
def main_page(request):
    if request.method == 'GET':
        params = request.GET

        logger.info('PARAMS {}'.format(params))

        input_params = {
            'name': params.get('name', ''),
            'author': params.get('author', ''),
            'year': params.get('year', ''),
            'place': params.get('place', ''),
            'type': params.get('type', ''),
            'sort': params.get('sort', ''),
            'extra': params.get('extra', ''),
            'tabular': params.get('tabular', ''),
        }
        
        PAGE_COUNT = 50
        last_page = 0

        page = int(params.get('page', '1'))
        query = Q()

        if (input_params['name']):
            query &= Q(name__icontains = input_params['name'].lower())
        if (input_params['author']):
            query &= Q(author__name__icontains = input_params['author'].lower())
        if (input_params['year']):
            query &= Q(date__icontains = input_params['year'].lower())
        if (input_params['place']):
            query &= Q(place__name__icontains=input_params['place'].lower())
        if (input_params['type']):
            query &= Q(object_type__name__icontains=input_params['type'].lower())
        if (input_params['extra']):
            query &= Q(info__icontains=input_params['extra'].lower())
        if (input_params['tabular']):
            query &= Q(tabular__icontains=input_params['tabular'].lower())

        all = DestinyObject.objects.filter(query)
        if input_params['sort'] == 'desc':
            all = all.order_by('-name')
        else:
            all = all.order_by('name')
        
        all = list(all)
        

        count_all = len(all)
        

        destiny_objects = all[(
            (page - 1) * PAGE_COUNT) : ((page - 1) * PAGE_COUNT + PAGE_COUNT + 1)]

        if len(destiny_objects) < PAGE_COUNT:
            last_page = 1
            destiny_objects = list(destiny_objects)
        else:
            destiny_objects.pop()

        for destiny in destiny_objects:
            pictures = PhotoItem.objects.filter(photo_item = destiny)

            # optimize_pictures(pictures)
            if len(pictures):
                destiny.picture = pictures[0]
        
        types = ObjectType.objects.all()
        faculties = Place.objects.all()

        return render(request, 'main.html', { 
            'page': page, 
            'first_page': page == 1,
            'last_page': last_page,
            'destiny_objects': destiny_objects,
            'types': types,
            'faculties': faculties,
            'count': count_all,
            'placeholders': input_params,
            'is_admin': request.user.is_staff
        })


@login_required(login_url='/auth')
def serve_image(request, uri):
    if not os.path.exists(os.path.join(MEDIA_ROOT, uri)):
        raise Http404("Изображения не существует")
        
    with open(os.path.join(MEDIA_ROOT, uri)) as f:
        content = f.read()
        return HttpResponse(content, content_type="image/png")


def safe_serve_image(request, uri):
    if not os.path.exists(os.path.join(MEDIA_ROOT, uri)):
        raise Http404("Изображения не существует")
        
    with open(os.path.join(MEDIA_ROOT, uri)) as f:
        content = f.read()
        return HttpResponse(content, content_type="image/png")


@login_required(login_url='/auth')
def photo_page(request, id):
    if request.method == 'GET':
        params = request.GET
        try:
            destiny = DestinyObject.objects.get(id=id)
        except Exception as e:
            raise Http404("Пользователя не существует")
        
        photo = PhotoItem.objects.filter(photo_item = destiny)
        if destiny.info:
            destiny.text = '<br>'.join(destiny.info.split('\n'))

        # optimize_pictures(photo)

        edit = params.get('edit', False) if request.user.is_staff else False
        return render(request, 'photo.html', { 
            'destiny': destiny, 
            'photo': photo, 
            'edit': edit, 
            'is_admin': request.user.is_staff,
            'authors': Author.objects.all().order_by('name'),
            'types': ObjectType.objects.all().order_by('name'),
            'places': Place.objects.all().order_by('name'),
        })


def login(request):
    if request.method == 'POST': 
        login_info = request.POST
        if not (login_info.get('email') and login_info.get('password')):
            return render(request, 'auth.html', { 'message': 'Неправильные данные для авторизации' })

        if request.user.is_authenticated():
            auth.logout(request)

        email = login_info['email'].lower().strip()
        try:
            query = Q()
            query &= (Q(username__iexact=email) | Q(email__iexact=email))
            user = User.objects.get(query)
        except Exception as e:
            return render(request, 'auth.html', {'message': 'Пользователя с таким email или логином не сущетсвует'})

        user = auth.authenticate(username = user.username, password = login_info['password'])
        if user is None:
            return render(request, 'auth.html', {'message': 'Неверный пароль'})

        auth.login(request, user)
        return HttpResponseRedirect('/')


def logout(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            auth.logout(request)
        return HttpResponseRedirect('/auth')


def optimize_pictures(pictures):
    for p in pictures:
        path = MEDIA_ROOT + p.photo.name
        if os.path.getsize(path) > 1024 * 1024:

            logger.warning("Optimizing image {} {} {} {}".format(
                path, MEDIA_ROOT, p.photo.name, os.path.getsize(path)))
            
            image = Image.open(path)
            k = 1024.0 / max(image.size)
            image = image.resize(
                (int(image.size[0] * k), int(image.size[1] * k)), Image.ANTIALIAS)
            image.save(path, optimize=True, quality=80)
            
            logger.warning("Optimized image {} {} {} {}".format(
                path, MEDIA_ROOT, p.photo.name, os.path.getsize(path)))


def handle_uploaded_file(f, path):
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@login_required(login_url='/auth')
def edit_object(request, id):
    if request.method == 'POST':
        if not request.user.is_staff:
            return HttpResponseRedirect('/item/'+id+'/')

        try:
            destiny = DestinyObject.objects.get(id=id)
        except Exception as e:
            return HttpResponseRedirect('/item/'+id+'/?edit=1')


        add_photo(request, id)
        name = request.POST.get('name', False)
        text = request.POST.get('text', False)
        date = request.POST.get('date', False)
        text = request.POST.get('text', False)
        tabular = request.POST.get('tabular', False)
        inventorized = True if request.POST.get('inventorized', False) else False

        try:
            author_name = request.POST.get('author', False)
            author = Author.objects.get(name=author_name)
        except Exception as e:
            author = Author.objects.create(name=author_name)
        try:
            place_name = request.POST.get('place', False)
            place = Place.objects.get(name=place_name)
        except Exception as e:
            place = Place.objects.create(name=place_name)
        try:
            object_type_name = request.POST.get('object_type', False)
            object_type = ObjectType.objects.get(name=object_type_name)
        except Exception as e:
            object_type = ObjectType.objects.create(name=object_type_name)

        if name != False:
            destiny.name = name
        if author != False:
            destiny.author = author
        if text != False:
            destiny.info = text
        if object_type != False:
            destiny.object_type = object_type
        if date != False:
            destiny.date = date
        if place != False:
            destiny.place = place
        if tabular != False:
            destiny.tabular = tabular
        destiny.inventorized = inventorized

        destiny.save()
        return HttpResponseRedirect('/item/'+id+'/')


@login_required(login_url='/auth')
def create_page(request):
    if request.method == 'GET':
        if not request.user.is_staff:
            return HttpResponseRedirect('/')

    return render(request, 'create.html', { 
        'edit': True,
        'authors': Author.objects.all().order_by('name'),
        'types': ObjectType.objects.all().order_by('name'),
        'places': Place.objects.all().order_by('name'),
    })


@login_required(login_url='/auth')
def create_object(request):
    if request.method == 'POST':
        if not request.user.is_staff:
            return HttpResponseRedirect('/')

        name = request.POST.get('name', False)
        text = request.POST.get('text', False)
        text = request.POST.get('text', False)
        date = request.POST.get('date', False)
        tabular = request.POST.get('tabular', False)
        inventorized = True if request.POST.get('inventorized', False) else False

        try:
            author_name = request.POST.get('author', False)
            author = Author.objects.get(name=author_name)
        except Exception as e:
            author = Author.objects.create(name=author_name)
        try:
            place_name = request.POST.get('place', False)
            place = Place.objects.get(name=place_name)
        except Exception as e:
            place = Place.objects.create(name=place_name)
        try:
            object_type_name = request.POST.get('object_type', False)
            object_type = ObjectType.objects.get(name=object_type_name)
        except Exception as e:
            object_type = ObjectType.objects.create(name=object_type_name)


        params = {}
        if name != False:
            params['name'] = name
        if author != False:
            params['author'] = author
        if text != False:
            params['info'] = text
        if object_type != False:
            params['object_type'] = object_type
        if date != False:
            params['date'] = date
        if place != False:
            params['place'] = place
        if tabular != False:
            params['tabular'] = tabular
        params['inventorized'] = inventorized

        destiny_object = DestinyObject.objects.create(**params)

        add_photo(request, str(destiny_object.id))
        return HttpResponseRedirect('/item/'+str(destiny_object.id)+'/')
        


@login_required(login_url='/auth')
def add_photo(request, id):
    if request.method == 'POST':
        if not request.user.is_staff:
            return HttpResponseRedirect('/item/'+id+'/')

        files = request.FILES

        for f in files.getlist('images'):
            name = str(randint(1, 100000000)) + f.name
            logger.info("NEW FILES {}".format(name))
            handle_uploaded_file(f, os.path.join(BASE_DIR, 'media/' + name))

            try:
                PhotoItem.objects.create(
                    photo = name,
                    photo_item = DestinyObject.objects.get(id=id),
                )
            except Exception as e:
                pass
        
        return HttpResponseRedirect('/item/'+id+'/?edit=1')
    
    
@login_required(login_url='/auth')
def delete_photo(request, id, photo_id):
    if request.method == 'GET':
        if not request.user.is_staff:
            return HttpResponseRedirect('/item/'+id+'/')

        try:
            PhotoItem.objects.get(id=photo_id).delete()
        except Exception as e:
            pass

        return HttpResponseRedirect('/item/'+id+'/?edit=1')


@login_required(login_url='/auth')
def delete_object(request, id):
    if request.method == 'GET':
        if not request.user.is_staff:
            return HttpResponseRedirect('/item/'+id+'/')

        try:
            DestinyObject.objects.get(id=id).delete()
        except Exception as e:
            pass

        return HttpResponseRedirect('/')

