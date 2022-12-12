from django.contrib import admin

# Register your models here.
from Home.models import PostModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']