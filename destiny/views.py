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
from msu_destiny.settings import BASE_DIR, STATIC_ROOT

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
            # return HttpResponseRedirect('/')
            return render(request, 'auth.html', params)
        else:
            return render(request, 'auth.html', params)

@login_required(login_url='/auth')
def main_page(request):
    if request.method == 'GET':
        params = request.GET

        PAGE_COUNT = 10
        last_page = 0

        page = int(params.get('page', '1'))
        t = params.get('type', '')
        place = params.get('place', '')
        
        all = DestinyObject.objects.all()
        count_all = len(all)

        destiny_objects = all[(
            (page - 1) * PAGE_COUNT): ((page - 1) * PAGE_COUNT + PAGE_COUNT + 1 + 1)]

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
            'place': place, 
            'type': t, 
            'destiny_objects': destiny_objects,
            'types': types,
            'faculties': faculties,
            'count': count_all
        })

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










