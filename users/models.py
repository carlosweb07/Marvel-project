from django.db import models

class Users(models.Model):
  name     = models.CharField(max_length=50)
  email    = models.CharField(max_length=80)
  password = models.TextField()
  is_admin = models.BooleanField(default=False)
  created  = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name + ' - ' + self.email