from rest_framework import serializers
from watchlistApp.models import watchList,streamingPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):
        review_user=serializers.StringRelatedField(read_only=True)
        class Meta:
                model=Review
                exclude=('movie',)
                # fields='__all__'

class MovieSerializer(serializers.ModelSerializer):
        #movie_desc=serializers.SerializerMethodField()
        review=ReviewSerializer(many=True,read_only=True)
        class Meta:
               model=watchList
               fields='__all__'

class StreamSerializer(serializers.ModelSerializer):
        watchlist=MovieSerializer(many=True,read_only=True)
        class Meta:
                model=streamingPlatform
                fields="__all__"


               #exclude=['name']
               #fields=['id','name']
        # def validate_name(self,value):
        #     if(len(value)<=2):
        #         raise serializers.ValidationError('Name is too short')
        #     return value
        # def get_movie_desc(self,object):
        #       return f'The description of {object.title} is {object.description}'

# def validate_name(value):
#     if(len(value)<=2):
#         raise serializers.ValidationError('Name chota hai')
#     return value

# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[validate_name])
#     description=serializers.CharField()
#     active=serializers.BooleanField()

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
    # def validate_name(self,value):
    #     if(len(value)<=2):
    #         raise serializers.ValidationError('Name is too short')
    #     return value
    # def validate(self,data):
    #     if(data['name']==data['description']):
    #         raise serializers.ValidationError('Name cannot be same as description')
    #     return data