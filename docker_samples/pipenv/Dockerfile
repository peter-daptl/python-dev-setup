FROM python:3.11

RUN pip install pipenv

RUN mkdir /opt/myapp

COPY . /opt/myapp

WORKDIR /opt/myapp

RUN pipenv install --deploy --ignore-pipfile
