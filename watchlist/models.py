from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class List(models.Model):
    movie_name = models.CharField(max_length=100)
    platform_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Stream {self.movie_name} on {self.platform_name}"


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(List, blank=True, related_name='list_items')

    def __str__(self):
        return f"{self.username} has stored {self.items}"
