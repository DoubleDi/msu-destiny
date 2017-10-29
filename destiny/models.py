# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DestinyObject(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Название Обьекта")
    author = models.CharField(max_length = 50, verbose_name = "Автор")
    info = models.TextField("text", blank = True, null = True)
    object_type = models.ForeignKey("ObjectType", verbose_name="Тип обьекта", blank = True, null = True)
    date = models.DateTimeField(verbose_name="Дата", blank=True, null=True)
    place = models.ForeignKey("Place", verbose_name="Место нахождения", blank=True, null=True)
    class Meta:
        verbose_name = "Обьект культуруного достояния"
        verbose_name_plural = "Обьекты культурного достояния"
        # indexes = [ models.Index(fields=[ 'name' ]), models.Index(fields=[ 'is_hidden', 'member_count' ]) ]
        
    def __unicode__(self):
        return self.name
    

class PhotoItem(models.Model):
    photo = models.ImageField(upload_to='photo/', blank=True, verbose_name="фото", null=True)
    comment = models.CharField(max_length=50, verbose_name="Комментарий")
    photo_item = models.ForeignKey("DestinyObject", verbose_name="Карточки")
    date = models.DateTimeField(verbose_name="Дата", blank=True, null=True)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __unicode__(self):
        return self.photo_item.name + " " + self.id


class ObjectType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип обьекта")

    class Meta:
        verbose_name = "Тип карточки"
        verbose_name_plural = "Типы карточек"

    def __unicode__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название места")

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __unicode__(self):
        return self.name

