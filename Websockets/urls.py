from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/',include('chat.urls')),
    path('',include('Webcam.urls')),
    path('',include('people_face.urls')),
    path('accounts/',include('accounts.urls')),
]