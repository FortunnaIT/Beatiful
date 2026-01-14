from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coment(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()
    text = models.TextField()


    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ism = models.CharField(max_length=50, null=True, blank=True)
    familya = models.CharField(max_length=50, null=True, blank=True)
    tug_sana = models.DateField(null=True,blank=True)
    foto = models.ImageField(upload_to='profil/',null=True,blank=True)
    nomer = models.CharField(max_length=13, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username