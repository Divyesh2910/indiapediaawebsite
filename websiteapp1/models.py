# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class PediaObject(models.Model):
    ObjectTitle=models.CharField(max_length=100)
    ObjectCat=models.CharField(max_length=100)
    Objectdesc=models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now=True)
    Objectimage=models.ImageField(upload_to='image/')

    def __str__(self):
        return self.ObjectTitle


class UserPedia(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class UserAdmin(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email
