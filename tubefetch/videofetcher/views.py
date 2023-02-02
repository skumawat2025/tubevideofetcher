from .models import Video
from .task import *
from rest_framework import viewsets
from .serializers import VideoSerializer

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

# ViewSet for the Video model
class VideoViewSet(viewsets.ModelViewSet):
    # Specify the queryset for Video model
    queryset = Video.objects.all().order_by('-published_datetime')
    # Specify the serializer class for Video model
    serializer_class = VideoSerializer

    # Function to list all Video objects
    def list(self, request):
        queryset = self.get_queryset()
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)
    
     # Function to create a new Video object
    def create(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Function to retrieve a Video object
    def retrieve(self, request, pk=None):
        queryset = Video.objects.all()
        video = get_object_or_404(queryset, pk=pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)
    
    # Function to update a Video object
    def update(self, request, pk=None):
        video = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Function to delete a Video object
    def destroy(self, request, pk=None):
        video = get_object_or_404(self.get_queryset(), pk=pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
