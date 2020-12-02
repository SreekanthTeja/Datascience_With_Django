from django.urls import path
from .views import imageform
urlpatterns=[
    path('face_recog/',imageform,name='picture'),
]