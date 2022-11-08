# Django Rest Framework IMDB App

```bash
# create python env
python3 -m venv djenv
# activate
source /djenv/bin/activate

# install django
pip install django

# check pip list installed
pip freeze

# create django project
django-admin startproject imdb

# create app
python manage.py startapp watchlist_app

# migrate / apply migration
python manage.py migrate

# create super user
python manage.py createsuperuser

# make migration after define model
python manage.py makemigrations

# django rest framework
pip install djangorestframework

# create super user
python3 manage.py createsuperuser
Username (leave blank to use 'tobil'): tobil
Email address: dev.suhada@gmail.com
Password: password
Password (again): password
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## Rereference

- [DRF]()
- [Status Code](https://www.django-rest-framework.org/api-guide/status-codes/)
- [django-relation-table](https://docs.djangoproject.com/en/3.1/topics/db/examples/)
