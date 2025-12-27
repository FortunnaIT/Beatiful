from django.db import models

# Create your models here.
class Reklama(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.name



class Mahsulot(models.Model):
    neme = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField()
    narx = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.neme


class Haqda(models.Model):
    text = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.text




