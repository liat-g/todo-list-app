##these are our paths to our web pages
from django.urls import path
from . import views

urlpatterns =[
    path("<int:id>", views.index, name="index"), ## the thing in the operators looks up the ToDoList by id, type a number
    path("",views.home, name="home"),
    path("create/", views.create, name="create")
]