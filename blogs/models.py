# run PYTHON MANAGE.PY MAKEMIGRATIONS <DB_NAME> after creating model
# then run PYTHON MANAGE.PY MIGRATE to migrate model schema to database

from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Blog(models.Model):
   # CASCADE - if realtor account gets removed its posts will be removed as well
   author = models.ForeignKey(Realtor, on_delete=models.CASCADE)
   subject = models.CharField(max_length=200)
   category = models.CharField(max_length=100)
   body = models.TextField()
   image = models.ImageField(upload_to='photos/%Y/%m/%d/')
   subject_date = models.DateTimeField(default=datetime.now, blank=True)

   # display subject title instead of a python object name in admin
   def __str__(self):
      return f"{self.subject} | {self.author}"
