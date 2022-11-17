from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Address(models.Model):
     trans_id = models.CharField(max_length=255)
     # address = models.CharField(max_length=255)
     # date = models.DateTimeField(default=datetime.now, blank=True)
     def __str__(self):
          return self.trans_id
     