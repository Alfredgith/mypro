from django.db import models

class has(models.Model):
      music=models.CharField(max_length=80)
      date=models.DateTimeField(auto_now_add=True)
