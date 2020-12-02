from django.urls import path
from .views import imageviewform,home,speechUI

urlpatterns=[
    path('',home,name='homepage'),
    path('image/',imageviewform,name='image'),
    path('speech/',speechUI,name='speak'),
    
]
