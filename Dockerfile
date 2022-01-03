FROM python:3
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/code \
    DJANGO_SETTINGS_MODULE=CvGenerator.settings \
    PORT=8000 \
    WEB_CONCURRENCY=3
# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential curl \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*
RUN addgroup --system django \
    && adduser --system --ingroup django django
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code
# Run as non-root user
RUN chown -R django:django /app
USER django
CMD gunicorn CvGenerator.wsgi:application