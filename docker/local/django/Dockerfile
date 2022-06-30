FROM python:3.10.0-slim-buster

ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# some reference information
LABEL maintainer='decong.yu@gmail.com'
LABEL description="Development image for drf-gis Project"

# set environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# dependency installlation, libgdal-dev for postGIS, ibpq-dev for postgres
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libgdal-dev \
    && apt-get install -y libpq-dev \
    && apt-get install -y gettext \
    && apt-get install -y netcat gcc postgresql \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# install python virtual environment
RUN pip3 install --upgrade pip
COPY ./requirements.txt /app/requirements.txt 
RUN pip3 install -r requirements.txt

# get entrypoint ready
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# get Django start ready
COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# get Celery start ready
COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

# get Flower start ready
COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower


ENTRYPOINT [ "/entrypoint"]
