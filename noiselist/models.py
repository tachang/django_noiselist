from django.db import models

# Create your models here.

# A single todo item. Only supports a single list.
class TodoItem(models.Model):
  name = models.CharField(max_length=256)
