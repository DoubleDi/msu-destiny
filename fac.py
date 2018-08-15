# -*- coding: utf-8 -*-

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "msu_destiny.settings")
django.setup()
import re
from destiny.models import ObjectType, DestinyObject, PhotoItem, ObjectType, Place, Author, Mol
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

do = DestinyObject.objects.filter(info__icontains='инв')

import re 

for d in do:
    n = re.search('Инв.*?(\d+)', d.info.encode('utf8'), flags=re.IGNORECASE)
    if n:
        print n.group(1)
    if not d.tabular and n:
        d.tabular = n.group(1)
        d.save()
