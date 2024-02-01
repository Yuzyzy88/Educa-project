# Pull official base Python Docker image
FROM python:3.10.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN apt update
RUN apt-get install build-essential libssl-dev python3-dev  gcc -y
RUN pip install -r requirements.txt

# Copy the Djando project
COPY . /code/
