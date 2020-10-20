from django.urls import path
from .views import imageviewform

urlpatterns=[
    # path('face/',facerecognition,name='face'),
    path('image/',imageviewform,name='image'),
    
]