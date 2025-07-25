from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),

    path("resume", views.resume, name="resume"),
    path("contact", views.contact, name="contact"),

    path("blog", views.blog, name="blog"),
    path("project", views.project, name="project"),
   
]


