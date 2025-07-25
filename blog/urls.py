from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("post/<int:pk>/like/", views.like_post, name="like_post"),
]