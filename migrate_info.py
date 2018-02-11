# -*- coding: utf-8 -*-
import os
import django
import imghdr
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "msu_destiny.settings")
django.setup()
from destiny.models import DestinyObject, PhotoItem, ObjectType, Place, Author

photos = PhotoItem.objects.all()

for photo in photos:
    if photo.info and len(photo.info):
        if photo.photo_item.info:
            photo.photo_item.info += "\n" + photo.info
        else:
            photo.photo_item.info = photo.info
        photo.photo_item.save()

