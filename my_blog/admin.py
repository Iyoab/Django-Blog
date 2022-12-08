from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from .models import *


class MyBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    #fields = ('title', 'slug', 'cat','content','photo', 'get_html_photo', 'is_published', 'created_at','updated_at')
    #readonly_fields = ('created_at','updated_at', 'get_html_photo')
    #save_on_top: bool = True
    

    # def get_html_photo(self, object):
    #     if object.photo:
    #         return mark_safe(f"<img src='{object.photo.url}' width=50>")

    # get_html_photo.short_description = 'Mini-image'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(MyBlog, MyBlogAdmin)
admin.site.register(Category, CategoryAdmin)

#admin.site.site_title = "Admin-panel of 'Characters' site"
#admin.site.site_header = "Admin-panel of 'Characters' site2"