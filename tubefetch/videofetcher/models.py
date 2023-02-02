from django.db import models

# Create your models here.

# A model to store the video data with a unique value of videoId
class Video(models.Model):
    # CharField to store the title of the video with a maximum length of 255 characters and allows Null values
    title = models.CharField(max_length=255, null=True)

    # TextField to store the description of the video and allows Null values
    description = models.TextField(null=True)

    # DateTimeField to store the published date and time of the video with a database index
    published_datetime = models.DateTimeField(db_index=True)

    # URLField to store the thumbnail URL of the video and allows Null values
    thumbnail_url = models.URLField(null=True)

    # TextField to store the videoId of the video and allows Null values with a unique constraint
    videoid = models.TextField(null=True, unique=True)

    # Overriding the default str representation of the model to return the title of the video
    def __str__(self):
        return self.title
    
    # Declaring the unique_together meta option to ensure the videoId is unique
    class Meta:
        unique_together = (("videoid",),)
