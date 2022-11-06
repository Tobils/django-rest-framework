from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


'''
class based view
list all, or create new
'''
class MovieList(APIView):
  def get(self, request, format=None):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

  def post(self,request, format=None):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)


'''
class based view
retrieve, update or delete an instance
'''
class MovieDetail(APIView):
  def get_object(self, id):
    try:
      return Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
      return Response({'Error':'Movie Not Found'}, status= status.HTTP_404_NOT_FOUND)
  
  def get(self, request, id, format=None):
    movie = self.get_object(id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, id, format=None):
    movie = self.get_object(id)
    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, id, format=None):
    movie = self.get_object(id)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


'''
function based view
@api_view(['GET'])
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



@api_view(['GET','PUT', 'DELETE'])
def movie_details(request, id):
  if request.method == 'GET':
    try:
      movie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
      return Response({'Error':'Movie Not Found'}, status= status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  if request.method == 'PUT':
    movie = Movie.objects.get(pk=id)
    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'DELETE':
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
'''