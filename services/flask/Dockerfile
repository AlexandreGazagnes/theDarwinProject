# base image python3.7 debian light
FROM python:3.7-buster

# switch to app and pip
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy the app
COPY . /app

# command
# ENTRYPOINT [ "python" ]
# CMD [ "wsgi.py" ]