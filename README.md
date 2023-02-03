# TubeFetcher

Welcome to the TubeFetcher project! This project is a combination of a React frontend and a Django backend, aimed to provide a seamless experience for users to fetch and view the latest videos on Youtube for a given query. Utilizing the Celery beat task scheduler, it is designed to be scalable and optimized for a better experience. We hope you find it as exciting as I do!

## Note

Please follow the instructions below to run this project, which includes both the React frontend and Django backend, as well as the Celery background task for displaying the latest video updates. If you encounter any issues, please refer to the accompanying video demonstration for running the app.

## Requirements

1. Node.js and npm (Node Package Manager)
2. Python3 and pip
3. Django

## Installation

The installation process for the TubeFetcher is split into two parts:
1. Installing the backend (tubefetch dir written in django)
2. Installing the frontend

## Installing the Backend

In order to run this app, you will need to create a YouTube Data v3 API key. Please follow these steps to obtain your API key:

1. Go to the [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started).
2. Create a new project or select an existing one
3. Enable the YouTube Data API v3
4. Create credentials for the API key.
5. Add the API key to the project in the appropriate location as specified below.

I have also added my youtube data API v3 for testing, but you can add you API credential over [here](https://github.com/18ME10049/tubevideofetcher/blob/7ca61c406547c103799f673bd8024cbd04beee63/tubefetch/tubefetch/settings.py#L153)

To install the Django backend of the TubeFetcher, follow these steps:
1. Open a terminal in the `tubefetch` folder of the project.
2. Run `pip install -r requirements.txt` to install all the required dependencies.
3. Run `python manage.py makemigrations` to create the database migrations.
4. Run `python manage.py migrate` to apply the migrations and create the database.
5. Run `python manage.py runserver` to start the development server.


## Installing the Frontend

To install the React frontend of the TubeFetcher, follow these steps:
1. Open a terminal in the `frontend` folder of the project.
2. Run `npm install` to install all the required dependencies.
3. Once the installation is complete, run `npm start` to start the development server.

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.


## Running the Celery background task 

Once the backend server is running properly and frontend is available in the localhost we need to To start the celery task and fetch the latest videos for a given query: 

 You can change the query from [here](https://github.com/18ME10049/tubevideofetcher/blob/7ca61c406547c103799f673bd8024cbd04beee63/tubefetch/videofetcher/task.py#L55) by whatever you want. 

 1. Open a new terminal window in the tubefetch directory.
 2. Run the following command to start scheduling the defined tasks in the project's backend: `celery -A tubefetch beat -l info`
 3. If the celery beat scheduler started we will be able to see after some time that the job is getting started to schedule leave this terminal window running. 
 4. Open a new terminal window in the tubefetch directory to run the celery worker.
 4. To run the tasks, we need to start the celery worker that is also connected to the Redis server. `celery -A tubefetch worker -l info -P eventlet` 

    #### NOTE
    - you need to install redis cli for windows if you don't alredy have one. You can do this by downloading [this-repo](https://github.com/MicrosoftArchive/redis/releases/download/win-3.2.100/Redis-x64-3.2.100.msi) and install it. 
    - Now run you redis cli (Can be found here - C:\Program Files\Redis\redic-cli)
    - check the host name of redis server and make sure it matches with this [code-line](https://github.com/18ME10049/tubevideofetcher/blob/7ca61c406547c103799f673bd8024cbd04beee63/tubefetch/tubefetch/settings.py#L146) if not replace this and the line below with the host name of your redis server. 

Now you should see your celery background task running at a period of 1 minute as mentioned [here](https://github.com/18ME10049/tubevideofetcher/blob/7ca61c406547c103799f673bd8024cbd04beee63/tubefetch/tubefetch/celery.py#L30)


That's all I hope you enjoyed and learned a new thing or two. Happy coding :)