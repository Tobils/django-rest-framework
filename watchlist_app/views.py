from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse

'''
manual without rest framework
'''
def movie_list(request):
  movies = Movie.objects.all() # Query Set --> iterable dictionary
  response = {
    'movies': list(movies.values())
  }
  return JsonResponse(response)

def movie_details(request, id):
  movie = Movie.objects.get(pk=id)
  response = {
    'id': movie.id,
    'name': movie.name,
    'description': movie.description,
    'active': movie.active
  }
  return JsonResponse(response)