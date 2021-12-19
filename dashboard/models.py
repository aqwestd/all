from django.db import models
from django.contrib.auth.models import  User
from django.utils import timezone
#from taggit.managers import TaggableManager

# Create your models here.
class Notes(models.Model):
 user=models.ForeignKey(User, on_delete=models.CASCADE)
 title = models.CharField(max_length=45)
 description = models.CharField(max_length=500) 
 
 def __str__(self):
     return self.title
 
 class Meta:
   verbose_name = "notes"
   verbose_name_plural ="notes"






class Homework(models.Model):
  user= models.ForeignKey(User,on_delete=models.CASCADE)
  subject = models.CharField(max_length=45)
  title = models.CharField(max_length=45)
  description = models.TextField()
  due = models.DateTimeField()
  is_finished=models.BooleanField(default=False)

  def __str__(self):
     return self.title


class Todo(models.Model):
  user= models.ForeignKey(User,on_delete=models.CASCADE)
  title = models.CharField(max_length=45)
  is_finished=models.BooleanField(default=False)
  def __str__(self):
    return self.title
   



