# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from destiny.models import DestinyObject, PhotoItem, ObjectType, Place, Author
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Q, Prefetch
from django.core import serializers
from django.core.mail import send_mail
from django.template.loader import render_to_string
from msu_destiny.settings import BASE_DIR, STATIC_ROOT, MEDIA_ROOT

import urllib
import logging
import json
import sys
import os

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

        logger.info('PARAMS', params)

        input_params = {
            'name': params.get('name', ''),
            'author': params.get('author', ''),
            'year': params.get('year', ''),
            'place': params.get('place', ''),
            'type': params.get('type', ''),
            'sort': params.get('sort', '')
        }
        
        PAGE_COUNT = 10
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

        all = DestinyObject.objects.filter(query)
        if input_params['sort'] == 'asc':
            all = all.order_by('name')
        if input_params['sort'] == 'desc':
            all = all.order_by('-name')
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
        })


@login_required(login_url='/auth')
def serve_image(request, uri):
    if not os.path.exists(os.path.join(MEDIA_ROOT, uri)):
        raise Http404("Изображения не существует")
        
    with open(os.path.join(MEDIA_ROOT, uri)) as f:
        content = f.read()
        return HttpResponse(content, content_type="image/png")


@login_required(login_url='/auth')
def photo_page(request, id):
    if request.method == 'GET':
        params = {}
        try:
            destiny = DestinyObject.objects.get(id=id)
        except Exception as e:
            raise Http404("Пользователя не существует")
        
        photo = PhotoItem.objects.filter(photo_item = destiny)
        for p in photo:
            p.text = '<br>'.join(p.info.split('\n'))
        
        return render(request, 'photo.html', {'destiny': destiny, 'photo': photo})

def login(request):
    if request.method == 'POST': 
        login_info = request.POST
        if not (login_info.get('email') and login_info.get('password')):
            return render(request, 'auth.html', { 'message': 'Неправильные данные для авторизации' })

        if request.user.is_authenticated():
            auth.logout(request)

        try:
            user = User.objects.get(username = login_info['email'])
        except Exception as e:
            return render(request, 'auth.html', {'message': 'Пользователя с таким email не сущетсвует'})

        user = auth.authenticate(username = login_info['email'], password = login_info['password'])
        if user is None:
            return render(request, 'auth.html', {'message': 'Неверный пароль'})

        auth.login(request, user)
        return HttpResponseRedirect('/')

def logout(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            auth.logout(request)
        return HttpResponseRedirect('/auth')










