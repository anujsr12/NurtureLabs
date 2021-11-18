from django.db import models

# Create your models here.
class Advisor(models.Model):
    name  = models.CharField(max_length = 100)
    profile_photo = models.ImageField(upload_to = 'pics')
    