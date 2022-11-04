from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
      movies = Movie.objects.all()
      print(movies.values())
      serializer = MovieSerializer(movies, many=True)
      return Response(serializer.data)
    
    if request.method == 'POST':
      serializer = MovieSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      else:
        return Response(serializer.errors)



@api_view()
def movie_details(request, id):
  movie = Movie.objects.get(pk=id)
  serializer = MovieSerializer(movie)
  return Response(serializer.data)