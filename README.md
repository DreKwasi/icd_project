# ICD_Codes

This project involves developing a RESTful API that can allows the user
to utilize an internationally recognized set of diagnosis codes.

## Getting Started with Setup

These instructions will cover usage information for postgres database setup and the docker container 

### Prerequisities

In order to run this container you'll need docker and postgres installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)
* [Postgres](https://www.postgresql.org/download/)

### Setting Up Postgres Database
Running this app will require a local database connection to Postgres. 
Steps for Setup
* After Cloning the Repository navigate to the docker-compose.yml
* Adjust the "db(service) environment" to your postgres settings i.e POSTGRES_DB, POSTGRES_USER and POSTGRES_PASSWORD
* Afterwards, navigate to the core/settings folder in your root directory
* For the "DATABASES" dictionary adjust the fields as before for name (same as POSTGRES_DB), user, password. (DO NOT EDIT THE HOST OR PORT)

This should get you up to date and started

#### Setting Up Docker Container

For running web client app on localhost(http://127.0.0.1:8000/api/) input the command below
to build images and containers needed and run the localhost

```shell
docker-compose up
```

Getting the python shell started and building tables in your DB

```shell
docker exec -it django_container /bin/bash
python manage.py migrate
```

Getting the postgres shell started

```shell
docker-compose exec psql-U postgres
```

## Getting Started with endpoints
* All routes for endpoints are available at http://127.0.0.1:8000/api
* icd.csv is a CSV file that contains ~10000 rows of data which can be uploaded using the endpoint; http://127.0.0.1:8000/api/codes/fileupload

## Bonus for emails
A Dummy email (mpharmatakehome@gmail.com, password:mpharmatakehome123) has been built for the purpose of notifications when 
data is uploaded as a CSV

## Built With

* python
* django
* django-rest framework

