from django.contrib import admin
from .models import Category, Profile, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'bio']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category']
    filter_horizontal = ['likes']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
