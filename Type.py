# -*- coding: utf-8 -*-
import os
import django
import imghdr
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "msu_destiny.settings")
django.setup()
import re

from destiny.models import DestinyObject, PhotoItem, ObjectType, Place, Author
# ObjectType.objects.create(
#     name = "Картина"
# )
#
# ObjectType.objects.create(
#     name = "Скульптура"
# )

# ObjectType.objects.all().delete()