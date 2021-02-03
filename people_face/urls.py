from django.urls import path
from .views import imageform
urlpatterns=[
    path('',imageform,name='picture'),
]