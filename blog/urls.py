from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.blogpost,name='blog'),
    path("<int:pk>/",views.blogdetail,name='details'),
    # path('', views.BlogListView.as_view(), name='blog'),
    # path('<int:pk>/', views.BlogDetailView.as_view(), name='details'),
    path('new/',views.BlogCreateView.as_view(), name='post_new'),
    path('<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
]