# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import sys

from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, User)
from django.db import models

logger = logging.getLogger('django')

# Create your models here.

# class DestinyUserManager(BaseUserManager):
#     def create_user(self, username, password1, password2):
#         if not username:
#             raise ValueError('Users must have a username')
#         user = self.model(
#             username=username,
#         )
#         if password1 != password2:
#             return None
#         user.set_password(password1)
#         try:
#             user.save()
#         except:
#             logger.error("Create user error")
#             return None
#         return user

#     def create_superuser(self, username, password):
#         user = self.model(
#             username=username,
#         )
#         user.set_password(password)
#         user.is_admin = True
#         user.save()
#         return user


# class DestinyUser(AbstractBaseUser):
#     username = models.CharField(max_length=50, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     can_edit = models.ManyToManyField(
#         "Place", blank=True, verbose_name="Подразделения, которые может изменять")
#     objects = DestinyUserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return str(self.username)

#     def __unicode__(self):
#         return u'{}'.format(self.username)

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin

#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"
        
#         # indexes = [models.Index(fields=['email']), models.Index(
#         #     fields=['is_hidden', 'name'])]

# class DestinyUser(AbstractUser):
#     can_edit = models.ManyToManyField(
#         "Place", blank=True, verbose_name="Какие подразделения может редактировать")

#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"
#         # indexes = [ models.Index(fields=[ 'name' ]), models.Index(fields=[ 'is_hidden', 'member_count' ]) ]


class DestinyObject(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Название Обьекта")
    author = models.ForeignKey("Author", verbose_name="Автор", blank=True, null=True)
    info = models.TextField("Информация", blank = True, null = True)
    object_type = models.ForeignKey("ObjectType", verbose_name="Тип обьекта", blank = True, null = True)
    date = models.CharField(max_length=50, verbose_name="Год", blank=True, null=True)
    place = models.ForeignKey("Place", verbose_name="Место нахождения", blank=True, null=True)
    class Meta:
        verbose_name = "Карточки"
        verbose_name_plural = "Карточка"
        # indexes = [ models.Index(fields=[ 'name' ]), models.Index(fields=[ 'is_hidden', 'member_count' ]) ]
        
    def __unicode__(self):
        return str(self.id) + " " + self.name
    

class PhotoItem(models.Model):
    photo = models.ImageField(upload_to='photo/', blank=True, verbose_name="фото", null=True)
    info = models.TextField("text", blank = True, null = True)
    # comment = models.CharField(max_length=50, verbose_name="Комментарий", blank = True, null = True)
    photo_item = models.ForeignKey("DestinyObject", verbose_name="Карточки")
    date = models.CharField(max_length=50, verbose_name="Год", blank=True, null=True)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __unicode__(self):
        return str(self.id) + " " + self.photo_item.name


class ObjectType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип обьекта")

    class Meta:
        verbose_name = "Тип карточки"
        verbose_name_plural = "Типы карточек"

    def __unicode__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название подразделения")
    users_to_edit = models.ManyToManyField(User, verbose_name="Пользователи, которые могут изменять подразделение", 
        blank=True, null=True)

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="ФИО автора")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __unicode__(self):
        return self.name
