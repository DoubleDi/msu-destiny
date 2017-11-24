# -*- coding: utf-8 -*-
import os
import django
import imghdr
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "msu_destiny.settings")
django.setup()
import re

from destiny.models import DestinyObject, PhotoItem, ObjectType, Place, Author


def parse(list, paste):
    # print(list)
    for i in list:
        path = paste + "/" + i
        if os.path.isfile(path) and imghdr.what(path) == None and path.rfind("_sorted.txt") != -1:
            destiny(path)

        elif os.path.isdir(path):
            parse(os.listdir(path), path)

    return

def destiny(path):
    with open(path, 'r') as f:
        all = f.readlines()
    name = all[1][:-1]
    # author = Author.objects.first(name__contains = all[0][1:-1])
    author = all[0][3:-1]
    # type = ObjectType.objects.get(name__contains = all[2][:-1])
    obj_type = all[2][:-1]
    obj_type = obj_type[0].upper() + obj_type[1:]
    date = get_date(path)
    place = all[3][:-1]
    # place = Place.objects.get(name__contains = all[3][:-1])
    print(obj_type)
    # print(obj_type.find("Скульптурa") != -1)
    if obj_type.find("Скульптурa") != -1:
        n = 1
    else:
        n = 2
    author = Author.objects.filter(name__contains=author)
    if author:
        author = author[0]
    else:
        author = ''
    DestinyObject.objects.create(
        name=name,  # Название картины
        author=author,  # Автор - надо достать обьект автора из базы по имени
        # "name__contains" проверяет на подстроку( чтобы точно найти).
        # Важно что get должен вернуть 1 обьект иначе он упадет исключением для нескольких есть filter
        object_type=ObjectType.objects.get(id = n),
        date=date,
        place=Place.objects.get(name__contains=place)
    )


def get_date(path):
    path = path[:path.rfind("_sorted.txt")] + ".txt"
    with open(path, 'r') as f:
        all = f.readlines()
    date = ""
    for i in all:
        b = re.findall('(\d+)', i)
        if b:
            for j in b:
                if len(j) == 4 and j[0] == '1' and  j[1] == '9'  and len(b) == 1 and i.find("к.") == -1 and i.find("ком.") == -1 and i.find("№") == -1:
                    date = j
                n = i.find(j + "г.")
                if n != -1:
                    if len(j) != 4:
                        date = "19" + j
                    else:
                        date = j
    return date

base = "media/Военное дело_sorted/Культурное достояние МГУ"
dir = os.listdir(base)
parse(dir, base)