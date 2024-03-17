from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .form import Movie_form
from .models import Movie_data, UserReviews

# Create your views here.

def home(request):
    mov = Movie_data.objects.all()
    return render(request, 'home.html', {"Movie_list" : mov})


# taking user postes separatly for editing--------------------------------------------------------------

def home_second(request):
    try:
        mov = Movie_data.objects.all().filter(added_by=request.user)
    except Exception as e:
        raise e

    return render(request, 'home_second.html', {'Movie_list_user': mov})


# categorations-----------------------------------------------------------------------------

#def movie_category(request):
 #   categories = Category.objects.all()
  #  return render(request, 'movies/category_dropdown.html', {'categories': categories})

# Registration, Login, Logout-----------------------------------------------------------------------------

def login(request):
    if request.method == 'POST':
        un = request.POST.get('l_name',)
        pa = request.POST.get('l_password',)
        mov_auth = auth.authenticate(username=un, password=pa)

        if mov_auth is not None:
            auth.login(request, mov_auth)
            return redirect('movieapp:home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('movieapp:login')

    return render(request, 'Login.html')

def register(request):
    if request.method == 'POST':
        un = request.POST.get('name',)
        fn = request.POST.get('first_name',)
        ln = request.POST.get('last_name',)
        email = request.POST.get('email',)
        pa = request.POST.get('password',)
        cp = request.POST.get('c_password',)

        if pa == cp:
            if User.objects.filter(username=un).exists():
                messages.info(request, "Username Taken")
                return redirect('movieapp:register')
            else:
                mov_reg = User.objects.create_user(username=un, first_name=fn, last_name=ln, email=email, password=pa)
                mov_reg.save()
                print("user created")
                messages.info(request, "Successfully Registered")
                return redirect('movieapp:login')
        else:
            messages.info(request, "Password not maching confirm password")
            return redirect('movieapp:register')


    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


# adding, updating, Deleting processes------------------------------------------------------------------

def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        desc = request.POST.get('desc',)
        release_date = request.POST.get('release_date',)
        actor = request.POST.get('actor',)
        cat_key =request.POST.get('categroy',)
        youtube = request.POST.get('youtube',)
        poster = request.FILES['poster']

        mov = Movie_data(name=name, desc=desc, release_date=release_date, actors=actor, category=cat_key, youtube_link=youtube, poster=poster)
        # adding the user who posted this post
        mov.added_by = request.user
        mov.save()
        return redirect('movieapp:home_second')

    return render(request, 'add.html')


def update(request, id):
    mov= Movie_data.objects.get(id=id)
    form = Movie_form(request.POST or None, request.FILES or None, instance=mov)
    if form.is_valid():
        form.save();
        return redirect('movieapp:home_second')

    return render(request, 'edit.html', {'form': form, 'movie_list': mov})


def delete(request, id):
    if request.method == "POST":
        mov = Movie_data.objects.get(id=id)
        mov.delete()
        return redirect('movieapp:home_second')

    return render(request, "delete.html")


  # Reviewing and rating movies and displaying them----------------------------------------------------------------------------

def review_movie(request, id):
    if request.method == 'POST':
        review = request.POST.get('review', )
        rating = request.POST.get('rating',)

        mov = UserReviews(content=review, rating=rating)
        # adding movie_id to which review is posted----------------
        mov.review_id = id
        mov.save()
        return redirect('/')

    return render(request, 'review.html')

def display_review(request, id):
    try:
        mov = UserReviews.objects.all().filter(review_id=id)
    except Exception as e :
        raise e

    return render(request, 'display_review.html', {'Movie_list_review' : mov})

# category details------------------------------------------------------------------

def movie_categroy(request, id):
    try:
        mov = Movie_data.objects.all().filter(category=id)
    except Exception as e:
        raise e

    return render(request, 'categroy.html', {'movie_list_cat' : mov})