# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "msu_destiny.settings")
django.setup()
import re
from destiny.models import DestinyObject, PhotoItem, ObjectType, Place, Author
# обьекты проекта, юзер тебе не нужен
# c полным списком полей можно при желании ознакомиться в destiny/models.py
# проверять на http://152807.simplecloud.ru/admin

# 1) Залить все типы обьектов (Картина, Скульптура и т д) 
ObjectType.objects.create(
    name = name  # Название типа обьекта 
)
# 2) Залить все факультеты (Картина, Скульптура и т д) 
Place.objects.create(
    name = name  # Название факультета 
)
# 3) Залить всех авторов 
Author.objects.create(
    name = name  # ФИО автора
)
# 4) Залить все обьекты культурного достоояния
DestinyObject.objects.create(
    name = name, # Название картины
    author = Author.objects.get(name__contains = substr), # Автор - надо достать обьект автора из базы по имени 
     #"name__contains" проверяет на подстроку( чтобы точно найти). 
     # Важно что get должен вернуть 1 обьект иначе он упадет исключением для нескольких есть filter
    object_type = ObjectType.objects.get(name__contains = substr),
    date = date,
    place = Place.objects.get(name__contains = substr)
)

# 5) Залить все Картинки с описаниями
PhotoItem.objects.create(
    photo = "path/to/photo.jpg", # предварительно на сервер в папочку media надо залить фотки и в photo надо записать путь относительно папочки media 
    info = text,  # просто весь текст который мы печатали
    photo_item = DestinyObject.objects.get(name__contains = substr), # обьект культурного достояния
    # или photo_item = DestinyObject.objects.get(id = id),
    date = date # год в формате строки например 1964
)
 # много фоток могут относиться к одному обьекту это норм
