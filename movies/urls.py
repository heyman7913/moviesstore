from django.urls import path
from . import views
from .views import petition_list, create_petition, vote_petition

urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/review/create/', views.create_review, name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', views.edit_review, name='movies.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.delete_review, name='movies.delete_review'),
    path('requests/', views.movie_requests, name='movie_requests'),
    path('requests/delete/<int:request_id>/', views.delete_movie_request, name='delete_movie_request'),
    path('petitions/', petition_list, name='petition_list'),
    path('petitions/create/', create_petition, name='create_petition'),
    path('petitions/<int:petition_id>/vote/', vote_petition, name='vote_petition'),
]