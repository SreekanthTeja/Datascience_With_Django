from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/',include('chat.urls')),
    path('',include('faceapp.urls')),
    path('face_recog/',include('people_face.urls')),
    path('blog/',include('blog.urls')),

]
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
    