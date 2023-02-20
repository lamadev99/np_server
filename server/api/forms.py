# forms.py
from django import forms
from django.contrib import admin
from api.models import News
from django.forms import Textarea

class NewsForm(forms.ModelForm):
    my_field = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = News
        fields = '__all__'