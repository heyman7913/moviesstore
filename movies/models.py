from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movies_images/')
    def __str__(self):
        return str(self.id) + ' - ' + self.name

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name

class MovieRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    requested_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-requested_at']

    def __str__(self):
        return f"{self.title} - {self.user.username}"

class Petition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    movie_name = models.CharField(max_length=200)
    director = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_petitions')
    created_at = models.DateTimeField(auto_now_add=True)
    voters = models.ManyToManyField(User, blank=True, related_name='voted_petitions')

    def __str__(self):
        return f"Petition: {self.movie_name}"

    @property
    def vote_count(self):
        return self.voters.count()

    def has_user_voted(self, user):
        return self.voters.filter(id=user.id).exists()