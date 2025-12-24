from django.contrib import admin

# Register your models here.
from .models import CategoryProject, Project, CategoryPost, Post, CategoryTag, PostTag
admin.site.register(CategoryProject)
admin.site.register(CategoryPost)
admin.site.register(Post)
admin.site.register(CategoryTag)
admin.site.register(PostTag)
admin.site.register(Project)