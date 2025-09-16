from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review, MovieRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def index(request):
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()
    template_data = {}
    template_data['movies'] = movies
    template_data['title'] = 'Movies'
    return render(request, 'movies/index.html', {'template_data':template_data})

def show(request, id):
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=movie)
    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    template_data['reviews'] = reviews
    return render(request, 'movies/show.html',
                  {'template_data': template_data})

@login_required
def create_review(request, id):
    if request.method == 'POST' and request.POST['comment']!= '':
        movie = Movie.objects.get(id=id)
        review = Review()
        review.comment = request.POST['comment']
        review.movie = movie
        review.user = request.user
        review.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)

@login_required
def edit_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user:
        return redirect('movies.show', id=id)
    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit Review'
        template_data['review'] = review
        return render(request, 'movies/edit_review.html',
            {'template_data': template_data})
    elif request.method == 'POST' and request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)

@login_required
def delete_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id,
        user=request.user)
    review.delete()
    return redirect('movies.show', id=id)

@login_required
def movie_requests(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')

        if title:
            MovieRequest.objects.create(
                user=request.user,
                title=title,
                description=description
            )
            messages.success(request, 'Movie request submitted successfully!')
        else:
            messages.error(request, 'Movie title is required!')

        return redirect('movie_requests')

    user_requests = MovieRequest.objects.filter(user=request.user)
    template_data = {
        'title': 'Movie Requests',
        'user_requests': user_requests
    }
    return render(request, 'movies/movie_requests.html', {'template_data': template_data})

@login_required
def delete_movie_request(request, request_id):
    movie_request = get_object_or_404(MovieRequest, id=request_id, user=request.user)
    movie_request.delete()
    messages.success(request, 'Movie request deleted successfully!')
    return redirect('movie_requests')