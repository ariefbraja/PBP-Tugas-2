from django import forms
from .models import Task
    
class TodolistForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('user', 'is_finished', )