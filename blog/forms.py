# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:37:26 2015

@author: cp
"""

from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)