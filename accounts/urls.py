from django.urls import path

from . import views


urlpatterns=[
    path('register/',views.register,name='signup'),
    path('signin/',views.signin,name='login'),
    path('logout/',views.logout_view,name='logout-user'),

]
