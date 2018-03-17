# Build an debian image
FROM python:3.6

# Install SO dependecies
RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pip \
    libpq-dev \
    python3-setuptools \
    gettext \
    vim \
    build-essential \
    postgresql \
    postgresql-contrib

# Install pip dependecies
RUN pip3 install --upgrade pip

# Crate user developer
RUN useradd -ms /bin/bash developer

# Create software folder
RUN mkdir /home/developer/software
WORKDIR /home/developer/software
ADD . /home/developer/software
RUN pip3 install -r requirements.txt

# Config user developer
USER developer
