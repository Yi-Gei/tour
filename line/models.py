from django.db import models
from tour import settings
from visitor.models import Visitor
class City(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField(null = True,blank=True)
    

class Viewspot(models.Model):
    city=models.ForeignKey(City)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    desc=models.TextField(null = True,blank=True)
    
class Hotel(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    desc=models.TextField(null = True,blank=True)
    city=models.ForeignKey(City)
    
    
class Restau(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    desc=models.TextField(null = True,blank=True)
    city=models.ForeignKey(City)
    
    
    
class Linepoint(models.Model):
    day=models.IntegerField(default=1)
    position=models.ForeignKey(Viewspot)
    
class Line(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField(null = True,blank=True)
    points=models.ManyToManyField(Linepoint)
    

    
    
       
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title=models.CharField(max_length=20)
    content=models.TextField(null = True,blank=True)
    publish_date=models.DateTimeField(auto_now_add=True)
    modify_date=models.DateTimeField(auto_now=True,auto_now_add=True)
    viewspot=models.ForeignKey(Viewspot)
    hotel=models.ForeignKey(Hotel)
    restau=models.ForeignKey(Restau)

class Img(models.Model):
    url=models.URLField()
    hotel=models.ForeignKey(Hotel)
    restau=models.ForeignKey(Restau)
    city=models.ForeignKey(City) 
    
class Status(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content=models.TextField(null = True,blank=True)
    publish_date=models.DateTimeField(auto_now_add=True)
    modify_date=models.DateTimeField(auto_now=True,auto_now_add=True)
