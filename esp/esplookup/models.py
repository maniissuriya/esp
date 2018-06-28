from django.db import models

# Create your models here.

class Jobdb (models.Model):
    jobnames = models.CharField(max_length=50)
    action = models.CharField(max_length=20)
    result = models.TextField()
    user = models.CharField(max_length=50)
    action_time = models.TextField()
    status = models.BinaryField()
