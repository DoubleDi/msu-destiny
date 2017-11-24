# -*- coding: utf-8 -*-
import os
import django
import imghdr
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "msu_destiny.settings")
django.setup()
import re

def parse(list, paste):
    # print(list)
    for i in list:
        path = paste + "/" + i
        if os.path.isfile(path) and imghdr.what(path) == None and path.rfind("_sorted.txt") == -1:
            parse_photo(path)

        elif os.path.isdir(path):
            parse(os.listdir(path), path)

    return

def parse_photo(path):
    with open(path, 'r') as f:
        text = f.read()
    date = get_date(path)
    photo = path[:path.rfind(".txt")] + ".jpg"
    substr = path[path.rfind("/") + 1 :path.rfind(".txt")]

    PhotoItem.objects.create(
        photo=photo,
        # предварительно на сервер в папочку media надо залить фотки и в photo надо записать путь относительно папочки media
        info=text,  # просто весь текст который мы печатали
        photo_item=DestinyObject.objects.get(name__contains=substr),  # обьект культурного достояния
        # или photo_item = DestinyObject.objects.get(id = id),
        date=date  # год в формате строки например 1964
    )
    # print(photo, substr, date)
    return


def get_date(path):
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

base = "Культурное достояние МГУ"
dir = os.listdir(base)
parse(dir, base)