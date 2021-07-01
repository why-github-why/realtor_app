from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Post(models.Model):
   # current_date = datetime.now().strftime("%B %d, %Y")

   # CASCADE - remove posts when removing realtor from db
   author = models.ForeignKey(Realtor, on_delete=models.CASCADE)
   subject = models.CharField(max_length=200, default='Subject')
   category = models.CharField(max_length=100, default='Category')
   introduction = models.CharField(max_length=255, default='This is the introduction.')
   paragraph_title = models.CharField(max_length=100, blank=True)
   paragraph = models.TextField(default='This is a paragraph.')
   paragraph_title_2 = models.CharField(max_length=100, blank=True)
   paragraph_2 = models.TextField(blank=True)
   paragraph_title_3 = models.CharField(max_length=100, blank=True)
   paragraph_3 = models.TextField(blank=True)
   quote = models.TextField(blank=True)
   paragraph_title_4 = models.CharField(max_length=100, blank=True)
   paragraph_4 = models.TextField(blank=True)
   paragraph_title_5 = models.CharField(max_length=100, blank=True)
   paragraph_5 = models.TextField(blank=True)
   paragraph_title_6 = models.CharField(max_length=100, blank=True)
   paragraph_6 = models.TextField(blank=True)
   image = models.ImageField(upload_to='photos/%Y/%m/%d/')
   image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   image_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   subject_date = models.DateTimeField(default=datetime.now(), blank=True)

   def __str__(self):
      return f"{self.subject} | {self.author}"
