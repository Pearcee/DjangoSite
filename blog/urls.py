from django.urls import path
from . import views
urlpatterns = [
    path(r'', views.index,name='index'),
    path(r'about', views.about,name='about'),
    path(r'contact', views.contact,name='contact'),
    path(r'data', views.data, name='data'), 
]