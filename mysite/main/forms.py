from django import forms 

class CreateNewList(forms.Form): ##this is the class that will define our forms 
    name = forms.CharField(max_length=200)
    check = forms.BooleanField()