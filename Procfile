release: python manage.py migrate
web: gunicorn CvGenerator.wsgi
worker: celery -A CvGenerator worker -B --loglevel=info