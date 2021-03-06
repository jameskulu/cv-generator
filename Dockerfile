FROM python:3
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/code \
    DJANGO_SETTINGS_MODULE=CvGenerator.settings \
    PORT=8000 \
    WEB_CONCURRENCY=3
WORKDIR /code
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY . /code
CMD gunicorn CvGenerator.wsgi:application
ENTRYPOINT celery -A CvGenerator worker --loglevel=info