from watchlistApp.models import watchList,streamingPlatform,Review
from watchlistApp.api.serializer import MovieSerializer,StreamSerializer,ReviewSerializer

from django.shortcuts import get_object_or_404

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from watchlistApp.api.custom_permission import IsReviewUserOrReadOnly,IsAdminOrReadOnly


class reviewCreate(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk=self.kwargs['pk']
        watchlist=watchList.objects.get(id=pk)
        user=self.request.user
        queryset=Review.objects.filter(movie=watchlist,review_user=user)
        if queryset.exists():
            raise ValidationError('Review already exists')
        if(watchlist.total_ratings==0):
            watchlist.avg_rating=serializer.validated_data['rating']
        else:
            watchlist.avg_rating=(watchlist.avg_rating+serializer.validated_data['rating'])/2
        watchlist.total_ratings+=1
        watchlist.save()
        serializer.save(movie=watchlist,review_user=user)

class reviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(movie=pk)

class reviewListById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes=[IsReviewUserOrReadOnly]
# class reviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class reviewListById(mixins.RetrieveModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class reviewList(APIView):
#     def get(self,request):
#         platform=Review.objects.all()
#         return Response(ReviewSerializer(platform,many=True).data)
#     def post(self,request):
#         platform=ReviewSerializer(data=request.data)
#         if(platform.is_valid()):
#             platform.save()
#             return Response(platform.data)
#         else:
#             return Response(platform.errors)

# class reviewListById(APIView):
#     def get(self,request,ID):
#         try:
#             platform=Review.objects.get(id=ID)
#         except Review.DoesNotExist:
#             return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
#         serialize=ReviewSerializer(platform)
#         return Response(serialize.data,status=status.HTTP_200_OK)
#     def put(self,request,ID):
#         stream_m=Review.objects.get(id=ID)
#         stream_s=ReviewSerializer(stream_m,data=request.data)
#         if(stream_s.is_valid()):
#             stream_s.save()
#             return Response(stream_s.data)
#         else:
#             return Response(stream_s.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self,request,ID):
#         stream_m=Review.objects.get(id=ID)
#         stream_m.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class stream(viewsets.ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]

    queryset=streamingPlatform.objects.all()
    serializer_class=StreamSerializer

# class stream(viewsets.ViewSet):
#     def list(self, request):
#         queryset = streamingPlatform.objects.all()
#         serializer = StreamSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = streamingPlatform.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = StreamSerializer(user)
#         return Response(serializer.data)

# class streamList(APIView):
#     def get(self,request):
#         platform=streamingPlatform.objects.all()
#         return Response(StreamSerializer(platform,many=True).data)
#     def post(self,request):
#         platform=StreamSerializer(data=request.data)
#         if(platform.is_valid()):
#             platform.save()
#             return Response(platform.data)
#         else:
#             return Response(platform.errors)

# class streamListById(APIView):
#     def get(self,request,pk):
#         try:
#             platform=streamingPlatform.objects.get(id=pk)
#         except streamingPlatform.DoesNotExist:
#             return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
#         serialize=StreamSerializer(platform)
#         return Response(serialize.data,status=status.HTTP_200_OK)
#     def put(self,request,pk):
#         stream_m=streamingPlatform.objects.get(id=pk)
#         stream_s=StreamSerializer(stream_m,data=request.data)
#         if(stream_s.is_valid()):
#             stream_s.save()
#             return Response(stream_s.data)
#         else:
#             return Response(stream_s.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self,request,pk):
#         stream_m=streamingPlatform.objects.get(id=pk)
#         stream_m.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    

class totalWatchLists(APIView):
    permission_classes=[IsAdminOrReadOnly] 
    def get(self,request):
        movies=watchList.objects.all()
        serializers=MovieSerializer(movies,many=True)
        return Response(serializers.data)
    def post(self,request):
        serializers=MovieSerializer(data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
    
class watchListById(APIView):
    permission_classes=[IsAdminOrReadOnly]
    def get(self,request,pk):
        try:
            movie=watchList.objects.get(id=pk)
        except watchList.DoesNotExist:
            return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializers=MovieSerializer(movie)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        movie=watchList.objects.get(id=pk)
        serializers=MovieSerializer(movie,data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        movie=watchList.objects.get(id=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# @api_view (['GET','POST'])
# def movie_list(request):
#     if(request.method=='GET'):
#         movies=Movie.objects.all()
#         serializers=MovieSerializer(movies,many=True)
#         return Response(serializers.data)
#     if(request.method=='POST'):
#         serializers=MovieSerializer(data=request.data)
#         if(serializers.is_valid()):
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors)


# @api_view (['GET','PUT','DELETE'])
# def movie_id(request,ID):

#     if(request.method=='GET'):
#         try:
#             movie=Movie.objects.get(id=ID)
#         except Movie.DoesNotExist:
#             return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
#         serializers=MovieSerializer(movie)
#         return Response(serializers.data,status=status.HTTP_200_OK)
#     elif(request.method=='PUT'):
#             movie=Movie.objects.get(id=ID)
#             serializers=MovieSerializer(movie,data=request.data)
#             if(serializers.is_valid()):
#                 serializers.save()
#                 return Response(serializers.data)
#             else:
#                 return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif(request.method=='DELETE'):
#         movie=Movie.objects.get(id=ID)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


