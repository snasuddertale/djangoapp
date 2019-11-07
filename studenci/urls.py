from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('miasta/', views.miasta, name='miasta'),
	path('uczelnie/', views.uczelnie, name='uczelnie'),
	path('login/', views.loguj_studenta, name='login'),
	path('uczelnia/', views.dodaj_uczelnie, name='uczelnia'),
]