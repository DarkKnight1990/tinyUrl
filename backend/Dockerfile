FROM python:3.9.5

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN apt-get install -y ghostscript libgs-dev
RUN apt-get install -y libmagickwand-dev imagemagick --fix-missing
RUN apt-get install -y libpng-dev zlib1g-dev libjpeg-dev
RUN apt-get install -y vim
RUN apt-get install -y nano

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ARG USER_ID
ARG GROUP_ID

RUN addgroup --gid $GROUP_ID py3user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID py3user
USER py3user