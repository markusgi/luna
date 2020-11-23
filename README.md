# luna

Purpose
Project Luna is the result of a one week sprint of web development.
The app's purpose is providing a platform for uploading restaurants around the world.
With features like adding reviews, comments connected to unique profiles - luna comes to live.

Setup Guide
Project and Frontend

Install node: https://nodejs.org/en/download/

Update npm: $ sudo npm install -g npm@latest

Install Docker: https://docs.docker.com/get-docker/

Clone the repository: $ git clone git@gitlab.propulsion-home.ch:full-stack/batch-13-aug-2020/group-projects/scorpio/project-luna.git

Install all dependencies: $ cd frontend/ $ npm i

Start the frontend React app: $ cd frontend/ $ npm start

Test if the React app is running correctly by accessing "http://localhost:3000/"

Backend and Docker

Build the docker image: $ docker build -t registry.gitlab.propulsion-home.ch/full-stack/batch-13-aug-2020/group-projects/scorpio/project-luna .

Setup PyCharm with a remote interpreter for the docker container:


PyCharm settings > Build, Execution, Deployment > Docker > virtual path "/backend" and local path "C:\Users\MyUser\PycharmProjects\project-luna\backend"
PyCharm settings > Project > Add Interpreter > Docker Compose > Service: "backend" + Python interpreter path "/opt/conda/envs/backend/bin/python"
Make PyCharm Run/Debug configurations >

Script path: "C:\Users\MyUser\PycharmProjects\project-luna\backend\manage.py"
Command: runserver 0.0.0.0:8000

Path mapping: "C:/Users/alex_/PycharmProjects/project-luna/backend=/backend"


Make PyCharm Run/Debug configurations > Same as above with command makemigrations

Make PyCharm Run/Debug configurations > Same as above with command migrate



Test if the server is running correctly by accessing "http://localhost:8000/admin/"


Endpoints
Registration
/api/registration/ POST: Register new user by asking for email (a validation code will be send to given email).
/api/registration/validate/ POST: Validate the creation of new user with the code sent by email.
Auth
/api/auth/token/ POST: Get a new JWT by passing username and password.
/api/auth/token/refresh/ POST: Get a new JWT by passing an old still valid JWT.
/api/auth/token/verify/ POST: Verify a token by passing the token in the body.
/api/auth/password-reset/ POST: Reset users password by sending a validation code in a email.
/api/auth/password-reset/validate/ POST: Validate password reset token and set new password for the user.
Search
/api/search/ GET: Search for ‘restaurants’, ‘reviews’ or ‘users’. {type: ‘restaurants’, ‘search_string’: ‘Pub’}
Home
/api/home/ GET: Get a list of the four best rated restaurants for the home screen.
Restaurant
/api/restaurants/ GET: Get the list of all the restaurant.
/api/restaurants/new/ POST: Create a new restaurant.
/api/restaurants/category/int:category_id/ GET: Get the all the restaurants by category.
/api/restaurants/user/int:user_id/ GET: Get the all the restaurants created by a specific user in chronological order.
/api/restaurants/int:id/ GET: Get the details of a restaurant by providing the id of the restaurant.
/api/restaurants/int:id/ PATCH: Update a restaurant by id (only by owner or restaurant admin).
/api/restaurants/int:id/ DELETE: Delete a restaurant by id (only by owner or restaurant admin).
Reviews
/api/reviews/new/int:restaurant_id/ POST: Create new review for a restaurant.
/api/reviews/restaurant/int:restaurant_id/ GET: Get the list of the reviews for a single restaurant.
/api/reviews/user/int:user_id/ GET: Get the list of the reviews by a single user.
/api/reviews/int:review_id/ GET: Get a specific review by ID and display all the information.
/api/reviews/int:review_id/ PATCH: Update a specific review (only by owner).
/api/reviews/int:review_id/ DELETE: Delete a specific review (only by owner).
/api/reviews/like/int:review_id/ POST: Like a review.
/api/reviews/like/int:review_id/ DELETE: Remove like from the review.
/api/reviews/likes/ GET: Get the list of the reviews the current user liked.
/api/reviews/comments/ GET: Get the list of the reviews the current user commented.
Comments
/api/review/comment/int:user_id/ GET: Get all the comments from a single user.
/api/review/comment/new/int:review_id/ POST: Comment on the review.
/api/review/comment/int:comment_id/ DELETE: Delete the comment on the review.
Categories
/api/category/list/ GET: Get the list of all the categories.
Users
/api/me/ GET: Get the user profile.
/api/me/ PATCH: Update the user profile.
/api/users/list/ GET: Get all users.
/api/users/?search=str:search_string/ GET: Search for a user.
/api/users/int:user_id/ GET: get a specific user profile.
