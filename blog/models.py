from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Post(models.Model):
   # CASCADE - remove posts when removing realtor from db 
   author = models.ForeignKey(Realtor, on_delete=models.CASCADE)
   subject = models.CharField(max_length=200)
   subject_date = models.DateTimeField(default=datetime.now, blank=True)
   category = models.CharField(max_length=100)
   body = models.TextField()
   image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

   def __str__(self):
      return f"{self.subject} | {self.author}"
