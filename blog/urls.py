# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:53:49 2015

@author: cp
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]