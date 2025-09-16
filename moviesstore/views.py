from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from movies.models import MovieRequest

# ...existing views...

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
    return render(request, 'movie_requests.html', {'template_data': template_data})

@login_required
def delete_movie_request(request, request_id):
    movie_request = get_object_or_404(MovieRequest, id=request_id, user=request.user)
    movie_request.delete()
    messages.success(request, 'Movie request deleted successfully!')
    return redirect('movie_requests')