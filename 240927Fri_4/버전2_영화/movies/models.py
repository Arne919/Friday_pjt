from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image_address = models.ImageField(blank=True)

    def __str__(self):
        return self.name