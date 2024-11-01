from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='movies')  # 다대다 관계 추가

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')  # related_name 추가
    title = models.CharField(max_length=100)
    content = models.TextField()
