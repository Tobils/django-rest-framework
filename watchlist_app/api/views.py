from xml.dom import ValidationErr
from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


from rest_framework import generics
# from rest_framework import mixins

from rest_framework import viewsets
from django.shortcuts import get_object_or_404


# overwrite queryset
class ReviewCreate(generics.CreateAPIView):
  serializer_class = ReviewSerializer
  def perform_create(self, serializer):
    pk = self.kwargs['pk']
    movie = WatchList.objects.get(pk=pk)
    user = self.request.user
    review_user = Review.objects.filter(watchlist=movie, review_user=user)

    if review_user.exists():
      raise ValidationErr("You have already give the review !")
    
    return serializer.save(watchlist=movie, review_user=user)


class ReviewList(generics.ListAPIView):
  # queryset = Review.objects.all()
  permission_classes = [IsAuthenticated]
  serializer_class = ReviewSerializer
  
  def get_queryset(self):
    pk = self.kwargs['pk']
    return Review.objects.filter(watchlist=pk)
  


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer


# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#   queryset = Review.objects.all()
#   serializer_class = ReviewSerializer

#   def get(self, request, *args, **kwargs):
#       return self.retrieve(request, *args, **kwargs)


# model view set

class StreamPlatformSet(viewsets.ModelViewSet):
  queryset = StreamPlatform.objects.all()
  serializer_class = StreamPlatformSerializer

'''
# view set 

class StreamPlatformSet(viewsets.ViewSet):
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(user)
        return Response(serializer.data)

    def create(self, request):
      serializer = StreamPlatformSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      else:
        return Response(serializer.errors)
    
    def destroy(self, request, pk):
      platform = StreamPlatform.objects.get(pk=pk)
      platform.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
'''




class StreamPlatformAV(APIView):
  def get(self, request):
    platform = StreamPlatform.objects.all()
    serializer = StreamPlatformSerializer(platform, many=True, context={'request': request})
    return Response(serializer.data)

  def post(self, request):
    serializer = StreamPlatformSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)

class StreamPlatformDetails(APIView):
  def get_object(self, id):
    try:
      return StreamPlatform.objects.get(pk=id)
    except StreamPlatform.DoesNotExist:
      return Response({'Error':'Platform Not Found'}, status= status.HTTP_404_NOT_FOUND)
  
  def get(self, request, id):
    platform = self.get_object(id)
    serializer = StreamPlatformSerializer(platform, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, id, format=None):
    platform = self.get_object(id)
    serializer = StreamPlatformSerializer(platform, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, id, format=None):
    platform = self.get_object(id)
    platform.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):
  def get(self, request, format=None):
    movies = WatchList.objects.all()
    serializer = WatchListSerializer(movies, many=True)
    return Response(serializer.data)

  def post(self,request, format=None):
    serializer = WatchListSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)


class WatchDetail(APIView):
  def get_object(self, id):
    try:
      return WatchList.objects.get(pk=id)
    except WatchList.DoesNotExist:
      return Response({'Error':'Not Found'}, status= status.HTTP_404_NOT_FOUND)
  
  def get(self, request, id, format=None):
    movie = self.get_object(id)
    serializer = WatchListSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, id, format=None):
    movie = self.get_object(id)
    serializer = WatchListSerializer(movie, data=request.data)
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
      serializer = WatchListSerializer(movies, many=True)
      return Response(serializer.data)
    
    if request.method == 'POST':
      serializer = WatchListSerializer(data=request.data)
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
    serializer = WatchListSerializer(movie)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  if request.method == 'PUT':
    movie = Movie.objects.get(pk=id)
    serializer = WatchListSerializer(movie, data=request.data)
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