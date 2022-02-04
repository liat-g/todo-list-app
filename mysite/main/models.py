from django.db import models

# Create your models here.
class ToDoList(models.Model): ##creating a todolist model
    name = models.CharField(max_length=200) ##our field is a class attribute

    def __str__(self): ##a class method printing the name of the todoList
        return self.name

class Item(models.Model):
    todoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE) ## this is how we are setting up the relationship between the todolist item and the todolist
    text = models.CharField(max_length=300) ##always need a maxlength for CharField
    complete = models.BooleanField()

    def __str__(self):
        return self.text