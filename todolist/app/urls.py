from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('add/', views.add_todo, name='add_todo'),
   path('delete/<int:todo_id>', views.delete_todo, name='delete_todo'),
#    path('register/', views.register)
]