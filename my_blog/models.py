from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta
from django.utils import timesince, timezone

class MyBlog(models.Model):
    '''Модель поста'''
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    author = models.CharField(max_length=50, blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
   
    def get_absolute_url(self):
        return reverse('post', kwargs = {'post_slug': self.slug})

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-updated_at']


    def how_new(self):
        value = timezone.now()
        b = timedelta(days=2)
        if value - b < self.created_at:
            return 1
        else:
            return 0

class Category(models.Model):
    '''Модель категорий'''
    name = models.CharField(max_length=155, db_index=True, verbose_name="Category")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL') 

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs = {'cat_slug': self.slug})
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['id']