FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code/
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput --clear
COPY . /code/
CMD gunicorn CvGenerator.wsgi:application