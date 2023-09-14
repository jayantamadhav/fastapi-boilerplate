FROM python:3.8


# set work directory
WORKDIR /usr/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install --upgrade pip wheel setuptools 

RUN pip install -r /usr/src/requirements.txt

COPY ./app /usr/src/app

CMD uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000