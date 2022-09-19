from django.contrib import admin
from .models import Ad, Comment, Favorite
from taggit.models import Tag
# Register your models here.
admin.site.register(Ad)
admin.site.register(Comment)
admin.site.register(Favorite)
