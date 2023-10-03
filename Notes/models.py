from django.db import models

# Create your models here.
class signup(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=80)


class notes(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
