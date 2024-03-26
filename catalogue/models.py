from django.db import models
from django.contrib.auth.models import User

from .constants import SEXS

class Skills(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Weeknesses(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Hero(models.Model):
  name              = models.CharField(max_length=50)
  birth_date        = models.DateField()
  sex               = models.CharField(max_length=20, choices=SEXS, default="M")
  height            = models.DecimalField(decimal_places=2, max_digits=10)
  weight            = models.IntegerField()
  first_apparition  = models.CharField(max_length=50)
  history           = models.TextField()
  skills            = models.ForeignKey(Skills, on_delete=models.CASCADE)
  weeknesses        = models.ForeignKey(Weeknesses, on_delete=models.CASCADE)
  image             = models.ImageField(upload_to='catalogue/static/imgs')
  created           = models.DateTimeField(auto_now_add=True)
  user_created      = models.ForeignKey(User, on_delete=models.CASCADE)