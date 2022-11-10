from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review
from django.utils.timezone import now


class ReviewSerializer(serializers.ModelSerializer):
  review_user = serializers.StringRelatedField(read_only=True)
  class Meta:
    model = Review
    # fields = "__all__"
    exclude = ['watchlist']

class WatchListSerializer(serializers.ModelSerializer):
  reviews = ReviewSerializer(many=True, read_only=True)
  class Meta:
    model = WatchList
    fields = "__all__" 

class StreamPlatformSerializer(serializers.ModelSerializer): #HyperlinkedModelSerializer
  watchlist = WatchListSerializer(many=True, read_only=True) # nama field harus sesuai dengan nama model
  # watchlist = serializers.StringRelatedField(many=True)
  # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  # watchlist = serializers.HyperlinkedRelatedField(
  #       many=True,
  #       read_only=True,
  #       view_name='watch-details',
  #       lookup_field='id' # penyebab error jika tidak di tentukan field lookup nya
  #   )

  # url = serializers.HyperlinkedIdentityField(
  #       view_name='streamplatform-detail',
  #       lookup_field='id'
  #   )
  class Meta:
    model = StreamPlatform
    fields = "__all__"








# '''
# custom validator
# '''

# def name_length(value):
#   if len(value) < 2:
#     raise serializers.ValidationError("Name is too short bro!")
#   else:
#     return value



# class MovieSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   name = serializers.CharField(validators=[name_length])
#   description = serializers.CharField()
#   active = serializers.BooleanField()

#   def create(self, validated_data):
#     return Movie.objects.create(**validated_data)
  
#   def update(self, instance, validated_data):
#     instance.name = validated_data.get('name', instance.name)
#     instance.description = validated_data.get('description', instance.description)
#     instance.active = validated_data.get('active', instance.active)
#     instance.save()
#     return instance

#   '''
#   validate object
#   '''
#   def validate(self, data):
#     if data['name'] == data['description']:
#       raise serializers.ValidationError("Description and Name should be different!")
#     else:
#       return data

#   '''
#   validate field based
#   def validate_name(self, value):
#     if len(value) < 2:
#       raise serializers.ValidationError("Name is too short!")
#     else:
#       return value
#   '''