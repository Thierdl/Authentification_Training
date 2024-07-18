from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_model(models.Model):
  name = models.CharField(max_length=150)
  description = models.CharField(max_length=500)
  emails = models.EmailField(max_length=150, null=True, blank=True)
  save_date = models.DateTimeField(auto_now_add=True)
  user_s = models.ForeignKey(User, on_delete=models.CASCADE)
  

  def __str__(self) -> str:
    return f"{self.name} {self.description}"




