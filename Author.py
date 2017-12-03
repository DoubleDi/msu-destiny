# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "msu_destiny.settings")
django.setup()
import re
from destiny.models import DestinyObject, PhotoItem, ObjectType, Place, Author

base = "media/Военное дело_sorted/"
text = "list.txt"
with open(base + text, 'r') as f:
    all = f.readlines()
count = 0
set_authors = set()
for line in all:
    if count % 3 == 0:
        tmp = line[:line.find("\n")]
        if "\ufeff" in tmp:
            tmp = tmp[tmp.find("\ufeff") + 1:]
        if "None" in tmp:
            tmp = "Неизвестный автор"
            # print(tmp)
        set_authors.add(tmp)
    count += 1
authors = sorted(set_authors)

for name in authors:
    Author.objects.create(
        name = name  # ФИО автора
    )

