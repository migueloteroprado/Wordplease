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

### Execute development server

```shell
python manage.py runserver
```

---

## Web site

http://127.0.0.1:8000

URLS:

| URL | Description | Notes |
| ------- | --- | --- |
| ```/``` | Home page. List of latest posts, paginated | Shows only published posts (pub date <= current date), ordered by pub date descending |
| ```/login``` | Login | |
| ```/signup``` | Register a new user | |
| ```/logout``` | Logout | |
| ```/users``` | List of Users, paginated | |
| ```/users/<username>``` | List of blogs belonging to the user, paginated | |
| ```/blogs``` | List of all blogs, paginated | |
| ```/blogs/<blog_name>``` | List of posts in that blog, order by pub date descending | Shows all posts if logged user is the blog author or a super user, otherwise only published posts. The page includes a filter by category |
| ```/blogs/<blog_name>/<post_id>``` | Shows post detail | |

---

## API REST

#### Users

| URL | Operation | Description |
| --- | --- | --- |
| ```/api/1.0/users/``` | GET | List of users. Allowed only to superusers |
| ```/api/1.0/users/``` | POST | Register a new user |
| ```/api/1.0/users/<id>/``` | GET | Obtain user detail. Authentication required. Only allowed if authenticated user is a superuser or is the same that we are trying to obtain. |
| ```/api/1.0/users/<id>/``` | PUT | Update user data. Authentication required. Only allowed if authenticated user is a superuser or is the same that we are trying to modify. |
| ```/api/1.0/users/<id>/``` | DELETE | Delete a user. Authentication required. Only allowed if authenticated user is a superuser or is the same that we are trying to delete. |

#### Categories

| URL | Operation | Description | 
| --- | --- | --- |
| ```/api/1.0/categories/``` | GET | List of categories. |
| ```/api/1.0/categories/``` | POST | Add a new category. Only allowed to superusers. |
| ```/api/1.0/categories/<id>/``` | GET | Obtain category detail.|
| ```/api/1.0/categories/<id>/``` | PUT | Update category. Only allowed to superusers. |
| ```/api/1.0/categories/<id>/``` | DELETE | Delete a category. Only allowed to superusers. |

#### Blogs

| URL | Operation | Description | Search fields | Ordering fields |
| --- | --- | --- | --- | --- |
| ```/api/1.0/blogs/``` | GET | List of blogs, paginated, with post count of every one included. | author's username | name |
| ```/api/1.0/blogs/``` | POST | Add a new blog. Authentication required. Blog author will be the authenticated user. |
| ```/api/1.0/blogs/<id>/``` | GET | Obtain blog detail. |
| ```/api/1.0/blogs/<id>/``` | PUT | Update a blog. Authentication required. Only allowed if authenticated user is the blog author or a superuser. |
| ```/api/1.0/blogs/<id>/``` | DELETE | Delete a blog. Authentication required. Only allowed if authenticated user is the blog author or a superuser. |

#### Posts

| URL | Operation | Description | Search fields | Ordering fields | Filter fields |
| --- | --- | --- | --- | --- | --- |
| ```/api/1.0/posts/``` | GET | List of all posts, paginated. Only published posts will be returned | title, summary, body | pub_date, title | categories |
| ```/api/1.0/blogs/<blog_id>/posts/``` | GET | Post list of the specified blog, paginated. If user is authenticated and is the blog owner or superuser, all posts will be returned. Otherwise, only published posts | title, summary, body | pud_date, title | categories
| ```/api/1.0/blogs/<blog_id>/posts/``` | POST | Add a new post in the specified blog. Authentication required. Only allowed if authenticated user is the blog author or a superuser |
| ```/api/1.0/blogs/<blog_id>/posts/<post_id>/``` | GET | Obtain post detail. If the post is not published, it only will be returned if authenticated user is the author of the post or a superuser |
| ```/api/1.0/blogs/<blog_id>/posts/<post_id>/``` | PUT | Update a post. Authentication required. Only allowed if authenticated user is the post author or a superuser. |
| ```/api/1.0/blogs/<blod_id>/posts/<post_id>/``` | DELETE | Delete a post. Authentication required. Only allowed if authenticated user is the post author or a superuser. |

#### Images

| URL | Operation | Description | 
| --- | --- | --- |
| ```/api/1.0/image_upload/``` | GET | List of uploaded images. |
| ```/api/1.0/image_upload/``` | POST | Upload a new image. Authentication required. The image owner will be the authenticated user. |
| ```/api/1.0/image_upload/<id>/``` | GET | Obtain image detail. |
| ```/api/1.0/image_upload/<id>/``` | PUT | Update an image. Authentication required. Only allowed if authenticated user if the image owner or a superuser. |
| ```/api/1.0/image_upload/<id>/``` | DELETE | Delete an image. Authentication required. Only allowed if authenticated user if the image owner or a superuser. |

#### Examples



---

## Models

#### Category

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

#### Blog

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

#### Post

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    body = models.TextField()
    image = models.URLField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    creation_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField()
    last_modification = models.DateTimeField(auto_now=True)

#### Image

    image = models.ImageField(upload_to='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)