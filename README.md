# ICD_Codes

This project involves developing a RESTful API that can allows the user
to utilize an internationally recognized set of diagnosis codes.

## Getting Started

These instructions will cover usage information and for the docker container 

### Prerequisities


In order to run this container you'll need docker and postgres installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)
* [Postgres](https://www.postgresql.org/download/)

### Usage

#### Container Parameters

For running web client app on localhost(http://127.0.0.1:8000/api/) input the command below
to build images and containers needed and run the localhost

```shell
docker-compose up
```

Getting the python shell started

```shell
docker exec -it django_container /bin/bash
```

Getting the postgres shell started

```shell
docker-compose exec psql-U postgres
```

## Built With

* python
* django
* django-rest framework
