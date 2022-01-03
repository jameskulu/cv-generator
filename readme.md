# CV Generator

It is a web application where user can generate CV on a go.
Web App Url : https://cv-generator-task.herokuapp.com/

## Features

-   Authentication (Login / Signup)
-   Customized admin panel
-   CV generating using input fields
-   Edit, Delete and Download CV functionality

## Technologies

-   Python
-   Django
-   Postgres
-   Celery
-   RabbitMQ
-   Docker
-   Heroku

## Installation

1. Clone the repository using `git clone https://github.com/jameskulu/cv-generator.git` command in the terminal.
2. Create a `.env` file and copy from `.env.example` file and insert the values.
3. Create a new postgres database.
4. Migrate the database using `python manage.py migrate` command.
5. Run the server using `python manage.py runserver` command.

#### To access admin panel

username: james
password: madrids

#### Docker

if you have docker on your machine use command `docker-compose build` to build the application and `docker-compose up` to run the application.
