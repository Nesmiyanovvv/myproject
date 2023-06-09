from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('login/', views.user_login.as_view(), name='login'),
    path('logout/', views.user_logout.as_view()),
    path('registration/', views.user_registration.as_view(), name='registration'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]