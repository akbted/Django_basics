from django.contrib import admin

# Register your models here.
from .models import Category, TodoList

admin.site.register(Category)
admin.site.register(TodoList)