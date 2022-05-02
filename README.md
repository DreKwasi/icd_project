# ICD_Codes (http://127.0.0.1:8000/api/)

This project involves developing an API to enable the user View/Edit/Delete and even Upload Data on the ICD Codes. This project runs in a docker container
and hence will require a running version of docker installed.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

```
install docker
good internet to allow for installation of other components in the docker image and containers

```

### Installing

```
navigate to root directory of your cloned folder
run cmd/shell (ensure docker is installed)
run docker-compose up to launch a local version of the API after installation of the necessary containers are made
run python manage.py runserver to run the web app
```

## Running the tests
```
execute docker exec -it django_container /bin/bash to launch an interactive shell of the container in your shell.
ensure this is not the same shell you use for running the web app
```

## Built With

* django - The web framework used
* django-rest framework - The REST Framework for Endpoints
* docker - Container management


## Authors

* **Andrews Asamoah Boateng** 

