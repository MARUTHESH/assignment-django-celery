## Assignment on Django and Celery
An api which when given a list of urls as a post request and email,  downloads the urls as html, zips it and sends an email with zip file as  attachment.
Email trigeering of the zip file and scrapping of the html of the given website urls is done using celery and rabbitmq.

## Python setup

On Linux, execute the following commands (first time setup)
1. python --version
2. lsvirtualenv
3. mkvirtualenv bookreadersapp --python=python3
4. python --version
5. pip install -r requirements.txt

## Running the project
1. python manage.py migrate
2. python manage.py runserver 0:8000
3. open any of the browser and enter localhost:8000/api in url field

## Create the user
1. python manage.py createsuperuser

## Running the celery in background
1. celery -A assignment worker -B -l info &
