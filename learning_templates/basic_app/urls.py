from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from basic_app import views

# template tagging, we set a global variable
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
