from django.db import models

# Create your models here.

class Survey(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    you_own = models.CharField(max_length=300)
    business_name = models.CharField(max_length=300)
    business_website = models.CharField(max_length=300)
    social_media_profile = models.CharField(max_length=900)
