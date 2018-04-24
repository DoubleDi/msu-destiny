# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from destiny.models import Author, DestinyObject, ObjectType, PhotoItem, Place
from django.contrib import admin


class MemberInline(admin.TabularInline):
    model = PhotoItem
    extra = 0
    show_change_link = True

    fieldsets = (
        (None, {'fields': ('photo', 'id' )}),
        # (None, {'fields': ('photo', 'info' )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('photo', 'id'),
            # 'fields': ('photo', 'info'),
        }),
    )

    readonly_fields = ('photo', 'id')
    # readonly_fields = ('photo', 'info')

    def has_add_permission(self, request):
        return False

class DestinyObjectAdmin(admin.ModelAdmin):
    inlines = [MemberInline]
    
    def get_place_name(self, obj):
        return obj.place.name if obj.place else ''

    def get_author_name(self, obj):
        return obj.author.name if obj.place else ''

    search_fields = ['id', 'name', 'date', 'author__name', 'place__name']
    list_display = (
        'name', 
        'get_author_name',
        'get_place_name',
        'date', 
        'id',
    )
    
    # filter_horizontal = ("author", "place")
    # raw_id_fields = ("author", "place")
    # autocomplete_fields = ("author", "place")



class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = (
        'name',
        'id'
    )

class ObjectTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = (
        'name',
        'id'
    )

class PhotoItemAdmin(admin.ModelAdmin):

    def get_photo_item_name(self, obj):
        return obj.photo_item.name

    def get_author_name(self, obj):
        return obj.photo_item.author.name

    search_fields = ['photo_item__name', 'photo_item__author__name']
    list_display = (
        'get_photo_item_name',
        'get_author_name',
        'id',
    )

class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = (
        'name',
        'id',
    )

admin.site.register(Author, AuthorAdmin)
admin.site.register(DestinyObject, DestinyObjectAdmin)
admin.site.register(ObjectType, ObjectTypeAdmin)
admin.site.register(PhotoItem, PhotoItemAdmin)
admin.site.register(Place, PlaceAdmin)
# admin.site.register(Profile)




# Register your models here.
