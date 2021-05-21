from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('post/<int:id>/details', views.admin_single_posts, name="admin_single_post"),
    path('auction/statics', views.auction_static, name="auction_static"),
    path('get/data/', views.get_data, name="get_data"),
]