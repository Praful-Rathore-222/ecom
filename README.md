# Database schema:
This is just a database schema in which i have implemented some tables like category and product and we can perform crud operations through querysets.
# Technology Stack :
I have used in my application,

```
1. Python 3
2. Django 3
3. sqlite3 Database
```
# Project Structure :
```
.
├── books
│   ├── admin.py
│   ├── apps.py
│   ├── images
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── images
│   ├── 89.jpg
│   ├── asdf.jpg
│   ├── download.jpeg
│   ├── erey.jpg
│   └── images_4.jpeg
├── manage.py
└── products
    ├── __init__.py
    ├── __pycache__
    ├── settings.py
    ├── urls.py
    └── wsgi.py

```
# Running Locally
First, clone the repository to your local machine:

```
git clone https://github.com/Praful-Rathore-222/restapi.git

cd restapi
```

Install the requirements:

```
pip install -r requirements/dev.txt
```
Apply the database migrations:

```
python manage.py migrate
```

Load the initial data:
``
Create administrator/super user:
```
python manage.py createsuperuser 

```

Finally, run the development server:

```
python manage.py runserver
```

` The site will be available at 127.0.0.1:8000. `