from django.contrib.auth.models import User
from django.db import models



# Create your models here.


# Movie details table------------------------------------------------------------------------------
class Movie_data(models.Model):
    name = models.CharField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    release_date = models.DateTimeField(null=False)
    actors = models.CharField(max_length=500)
    youtube_link = models.TextField(blank=True)
    poster = models.ImageField(upload_to='Galary')
    category = models.IntegerField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# user table------------------------------------------------------------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

 # Review table------------------------------------------------------------------------------
class UserReviews(models.Model):
    review_id = models.IntegerField()
    content = models.TextField()
    rating = models.FloatField(null=True)

    def __str__(self):
        return self.review_id


