from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("portfolio", views.portfolio, name="portfolio"),
   
    path("resume", views.resume, name="resume"),
    path("contact", views.contact, name="contact"),
    path("starter-page", views.starter_page, name="starter_page"),
    path("blog", views.blog, name="blog"),
    
   
    
]


