FROM python:3.7-stretch
ENV PYTHONUNBUFFERED 1

RUN mkdir backend
WORKDIR /backend
COPY ./requirements ./requirements
RUN pip install --quiet -r requirements/prod.txt --no-cache-dir
COPY . .