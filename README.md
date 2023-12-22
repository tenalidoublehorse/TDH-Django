# TDH-Django
# TdhBackend


#install env
#pip install virtualenv
# create virtual environment
#python -m venv env-tdh

# activate virtual environment
#env-tdh\Scripts\activate

# install libs
pip freeze > requirements.txt 
pip install -r requirements.txt

# create django  project
Django-admin startproject "PROJECTNAME"

# create django app 
python manage.py startapp "APP NAME"

# create super user 
python manage.py createsuperuser
# migration process 
python manage.py makemigrations 

# run migrations 
python manage.py migrate 

# Run project or applications
python manage.py runserver



when create apis 
----------------
1. install - pip install django-cors-headers
2. INSTALLED_APPS = [
    # ...
    'corsheaders',
    # ...
]

3.MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
]
4.CORS_ALLOW_ALL_ORIGINS = True
5.CORS_ALLOWED_ORIGINS = [
    "https://yourfrontendapp.com",
    "https://anotherfrontendapp.com",
]