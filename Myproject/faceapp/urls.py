from django.urls import path
from .views import imageviewform

urlpatterns=[
    path('image/',imageviewform,name='image'),
    
]
