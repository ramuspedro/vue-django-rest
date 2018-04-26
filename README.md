# Django Quickstart

## Create the project
- In the root file create: *Dockerfile, requirements.txt, docker-compose.yml*

* Build the image
```sh
$ docker-compose run backend django-admin.py startproject project .

create app
$ docker-compose run backend django-admin.py startapp quickstart
```

* Change the ownership of the new files
```sh
$ sudo chown -R $user .
```

* Run: *docker-compose up*

* To run the migration on django: *docker-compose run backend python manage.py migrate*
or
* Enter on container and run *python manage.py migrate* (https://docs.djangoproject.com/pt-br/2.0/intro/tutorial02/)

* Access the app: *http://localhost:8000/*

* Create superuser: *python manage.py createsuperuser*

* Create an app: *python manage.py startapp app-project*

## Redo the project
- To erase what you've done so far:
```sh
$ docker-compose down
```

- remove the image of the project
```sh
$ docker rmi image_id --force

$ sudo rm -R manage.py project
```