# Wordplease

Django / REST Framework
Bootcamp Web V - Keepcoding

---

## Installation
You need [Python 3](https://www.python.org) to be installed on your computer
To install the application, execute the following commands on a terminal:

###### 1) Clone repository
```shell
git clone https://github.com/migueloteroprado/Wordplease.git
cd Wordplease
```
###### 2) Setup and activate the python virtual env

```shell
virtualenv env -p python3
source env/bin/activate
```

###### 3) Install the modules required:
```shell
pip install -r requirements.txt
```

###### 4) Create the Database:
```shell
python manage.py migrate
```

###### 5) Create a superuser:
```shell
python manage.py createsuperuser
```

###### 6) Run server
```shell
python manage.py runserver
```

---

## Website

http://127.0.0.1:8000

URLS:

| URL | Description | Notes |
| ------- | --- | --- |
| ```/``` | Home page. List of latest posts | Shows only published posts (pub date <= current date), order by pub date descending |
| ```/login``` | Login | |
| ```/signup``` | Register a new user | |
| ```/logout``` | Logout | |
| ```/users``` | List of Users | |
| ```/users/<username>``` | List of blogs belonging to the user | |
| ```/blogs``` | List of all blogs | |
| ```/blogs/<blog_name>``` | List of posts in that blog, order by pub date descending | Shows all posts if logged user is the blog author or a super user, otherwise only published posts. The page includes a category filter |
| ```/blogs/<blog_name>/<post_id>``` | Shows post detail | |

---

## API REST

| URL | Operation | Description |
| --- | --- | --- |
| ```/api/1.0/``` | GET | |
