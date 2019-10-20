# -*- coding: utf-8 -*-
from django import forms
from . import models

class SearchForm(forms.ModelForm):
    class Meta:
        model = models.Search
        fields = ['name','from_email','subject','message','receive_newsletter']
