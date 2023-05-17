from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.hello, name= 'hello'),
    path('hello/', views.hello, name= 'hello'),
    path('favorites/', views.favorites, name= 'favorites'),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name= 'contact'),

]