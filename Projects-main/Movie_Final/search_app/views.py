from django.shortcuts import render
from Movie_app.models import Movie_data, UserProfile
from django.db.models import Q

# Create your views here.

# This search is for search all movies--------------------------------------------------------------------------
def search(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        if query.isalnum():
            movies = Movie_data.objects.all().filter(Q(name__contains=query))


    return render(request,'search.html', {'query' : query, 'movies' : movies})



# Thsi search is for user posted movies all------------------------------------------------------------------------

def search_user(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        if query.isalnum():
            movies = Movie_data.objects.all().filter(Q(name__contains=query) & Q(added_by=request.user))

    return render(request,'search_second.html', {'query' : query, 'movies' : movies})