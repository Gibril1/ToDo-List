from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now_add = True)


    def __str__(self) -> str:
        return self.content
