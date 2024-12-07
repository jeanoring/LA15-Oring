from django.urls import path
from . import views

#URL Configuration
urlpatterns = [
    path('hello/', views.say_hello), 
    path('hi/', views.say_hi, name='hi'),
    path('posts/', views.blog_list, name='posts'),
     path('posts/<int:id>/', views.blog_detail, name='blog_detail'),
]
#itodati path('hi/', views.say_hi)
#bago ('hi/', views.say_hi, name='hi') 