from django.urls import path
from . import views


urlpatterns = [
    path('call_click/', views.call_click),
    path('boosts/', boosts, name='boosts')
]

boosts = views.BoostViewSet.as_view({
    'get': 'list',
    'post': 'create',
})