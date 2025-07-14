from django.db import models


class Blog(models.Model):
    blog_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.blog_text
class post(models.Model):
    title = models.CharField(max_length=200)
   
    def __str__(self):
        return self.title
   
    
class deleted(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.title