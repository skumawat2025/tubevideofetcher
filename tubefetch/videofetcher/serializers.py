from rest_framework import serializers
from .models import Video

# Define serializers for the Video model
class VideoSerializer(serializers.ModelSerializer):
    # Specify the model that should be used for serialization
    class Meta:
        model = Video
        # Include all fields in the serialization
        fields = '__all__'