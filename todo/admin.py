from django.contrib import admin

# Register your models here.

from todo.models import Todolist

admin.site.register(Todolist)
