# -*- coding: cp1251 -*-
from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Advertisement
from django.core.exceptions import ValidationError

class AdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['auction'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startwith('?'):
            raise ValidationError('��������� �� ����� ���������� � ��������������� �����')
        return title



