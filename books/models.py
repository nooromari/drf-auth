from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(default="", null=True)
    price = models.IntegerField()


    def __str__(self) -> str:
        return self.name