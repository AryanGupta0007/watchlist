from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_name = models.CharField(max_length=100)
    platform_name = models.CharField(max_length=100)
    def __str__(self):
        return f"Stream {self.movie_name} on {self.platform_name}"
