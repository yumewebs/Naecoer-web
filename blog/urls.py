from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('<int:post_id>/', views.post, name="post"),
    path('summernote/', include('django_summernote.urls')),
]