from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myapp/', views.myapp, name='myapp'),
    path('test/', views.test, name='test'),
    path('add_note/', views.add_note, name='add_note'),
]