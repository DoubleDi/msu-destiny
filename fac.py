# -*- coding: utf-8 -*-

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "msu_destiny.settings")
django.setup()
import re
from destiny.models import DestinyObject, PhotoItem, ObjectType, Place, Author

with open('all.txt', 'r') as f:
    all = f.readlines()

for name in all:
    Place.objects.create(
        name=name  # Название факультета
    )
    
