from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.home, name="index"),
    path('post/create', views.create_post, name="create_post"),
    path('posts/all', views.my_posts, name="my_post"),
    path('post/<int:id>/details', views.single_posts, name="single_post"),
]