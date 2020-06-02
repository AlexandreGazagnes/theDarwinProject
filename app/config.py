"""App configuration."""

import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

import redis


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    SESSION_COOKIE_NAME = os.environ.get("SESSION_COOKIE_NAME")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"

    # Flask-Session
    SESSION_TYPE = environ.get("SESSION_TYPE")
    # print(environ.get("SESSION_REDIS"))
    SESSION_REDIS = redis.from_url("redis://redis_session:6379")


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
    # DATABASE_URI = os.environ.get("PROD_DATABASE_URI")


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    SEND_FILE_MAX_AGE_DEFAULT = 0
    # DATABASE_URI = os.environ.get("DEV_DATABASE_URI")
