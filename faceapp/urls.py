from django.urls import path
from .views import imageviewform,home

urlpatterns=[
    path('',home,name='homepage'),
    path('image/',imageviewform,name='image'),
    
]
