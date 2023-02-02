# Importing required packages and modules
import logging
import socket
from django.db import IntegrityError
import googleapiclient.discovery
from requests import HTTPError
from .models import Video
from celery import shared_task
from django.conf import settings

# Initializing logger for error logging
logger = logging.getLogger(__name__)

# Server address and port for connection
SERVER_ADDRESS = "youtube.googleapis.com" #'142.250.67.138'
PORT = 80

# Developer keys from Django settings
DEVELOPER_KEYS = settings.DEVELOPER_API_KEY

# Celery task to update videos in the database
@shared_task
def update_videos_task():
    # Creating a socket connection
    sock = None
    try:
        sock = socket.create_connection((SERVER_ADDRESS, PORT), timeout=5)
        # Logging successful connection
        logger.info("Successful connection to {} on port {}".format(SERVER_ADDRESS, PORT))
    except socket.error as e:
        # Logging error in connection
        logger.error("Failed to connect to {} on port {}: {}".format(SERVER_ADDRESS,PORT, e))
        return

    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # API details for YouTube API
    api_service_name = "youtube"
    api_version = "v3"
    response = None

    # Loop to use different API keys in case one fails
    for api_key in DEVELOPER_KEYS:
        try:
            # Building YouTube API client
            youtube = googleapiclient.discovery.build(
                api_service_name, api_version, developerKey = api_key)
    
            # Making a search request for videos
            request = youtube.search().list(
                part="snippet",
                maxResults=30,
                order="date",
                publishedAfter="2023-01-31T09:00:37Z",
                q="official",
                safeSearch="moderate",
                type="video"
            )

            # Executing the API request
            response = request.execute()
            # Logging success of API request
            logger.info("Valid api key found processing the request")
            break
        except Exception as e:
            # Logging error in API request
            logger.error("Error making YouTube API request: {}".format(e))
            continue
    
    # Checking if API request was not successful with any API keys
    if response is None:
        logger.error("Error making YouTube API request with all API keys")
        # Closing the socket connection before finishing the task if open
        if sock:
            sock.close()
        return
    
    # Loop to store videos in the database
    for item in response['items']:
        try:
            # Creating Video object with API response data
            video = Video(
            title=item['snippet']['title'],
            description=item['snippet']['description'],
            published_datetime=item['snippet']['publishedAt'],
            thumbnail_url=item['snippet']['thumbnails']['default']['url'],
            videoid=item['id']['videoId']
            )
            # Saving the Video object
            video.save()
        except IntegrityError:
            # Logging info for IntegrityError for a entry in database
            logger.info("Video with videoid {} already exists - ignoring".format(item['id']['videoId']))
            pass
        except Exception as e:
            # Logging error if fails to save entry in database
            logger.error("Error saving video information to the database: {}".format(e))
            pass
    
    # Closing the socket connection if open
    if sock:
        sock.close()