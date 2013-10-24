from django.db import models

class City(models.Model):
    name=models.CharField(max_length=20)
    

class Viewspot(models.Model):
    city=models.ForeignKey(City)
    address=models.CharField(max_length=20)
    
class Hotel(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    city=models.ForeignKey(City)
    viewspot=models.ForeignKey(Viewspot)
    
class Restau(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    city=models.ForeignKey(City)
    viewspot=models.ForeignKey(Viewspot)

class Linepoint(models.Model):
    time=models.DateTimeField()
    viewspot=models.ForeignKey(Viewspot)
    hotel=models.ForeignKey(Hotel)
    restau=models.ForeignKey(Restau)
    line=models.ForeignKey(Line)

class Line(models.Model):
    name=models.CharField(max_length=20)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
   
    
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title=models.CharField(max_length=20)
    content=models.TextField(null = True,blank=True)
    publish_date=models.DateTimeField(auto_now_add=True)
    modify_date=models.DateTimeField(auto_now=True,auto_now_add=True)
    viewspot=models.ForeignKey(Viewspot)
    hotel=models.ForeignKey(Hotel)
    restau=models.ForeignKey(Restau)

    
class Status(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content=models.TextField(null = True,blank=True)
    publish_date=models.DateTimeField(auto_now_add=True)
    modify_date=models.DateTimeField(auto_now=True,auto_now_add=True)
