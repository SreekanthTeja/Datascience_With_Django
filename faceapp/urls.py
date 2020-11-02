from django.urls import path
from .views import imageviewform,home,message

urlpatterns=[
    path('',home,name='homepage'),
    path('msg/',message,name='message'),
    path('image/',imageviewform,name='image'),
    
]
