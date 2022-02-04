from django.shortcuts import render
##this stores our different views for our different applications and serves http requests
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

##this function represents a view
def index(response, id):
    ls = ToDoList.objects.get(id=id) ##this is how we get the todoList By id
    return render(response, "main/list.html", {"ls":ls}) ##this is how we are rendering our template, the dictionary is how we are passing variables

def home(response):
    return render(response, "main/base.html", {}) ##this is how we are rendering our template

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid(): ##if all the fields are valid, this will return true and saves the name to the db
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        
        return HttpResponseRedirect("/%i" %t.id) ##this redirects to the page that was just created

    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form":form})