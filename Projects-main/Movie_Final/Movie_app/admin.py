from django.contrib import admin
from . models import Movie_data, UserProfile, UserReviews

# Register your models here.

admin.site.register(Movie_data)
admin.site.register(UserProfile)
admin.site.register(UserReviews)