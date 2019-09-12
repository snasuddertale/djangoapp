from django.conf.urls import url

from . import views

urlspatterns = [
    path('', views.index)
]