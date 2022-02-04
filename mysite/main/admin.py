from django.contrib import admin
from .models import ToDoList, Item ##this is where we are registering our models
# Register your models here.

admin.site.register(ToDoList)
admin.site.register(Item)