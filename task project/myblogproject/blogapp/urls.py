from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='list'),
    path('<int:blog_id>/', views.blog_detail, name='detail'),
    path('<int:blog_id>/share_post/', views.share_post, name='share_post'),
    path('share_success/', views.share_success, name='share_success'),
    path('<int:blog_id>/add_comment/', views.add_comment, name='add_comment'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
]