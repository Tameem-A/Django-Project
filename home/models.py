from django.db import models

class Contact(models.Model):
    email=models.CharField(max_length=120)
    password=models.CharField(max_length=120)