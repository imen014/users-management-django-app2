from django.forms import ModelForm
from django.db import models
from django import forms
from model_app.models import Users


class MyModelForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username','password','email']

    
       