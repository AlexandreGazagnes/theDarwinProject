from flask import Flask, escape, request, flash, url_for, render_template, abort, redirect
# from flask import session, Session
#
# from flask_sqlalchemy import SQLAlchemy
# # from flask.ext.session import Session
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager, UserMixin
# from flask_mail import Mail
from flask import Blueprint
from app.forms import MyForm

home = Blueprint('home', __name__)


@home.route('/')
def welcome():

    return render_template('home.html', object = "Hello")


@home.route('/init', methods=["GET", "POST"])
def init() : 

# def register(request):
#     form = RegistrationForm(request.POST)
#     if request.method == 'POST' and form.validate():
#         user = User()
#         user.username = form.username.data
#         user.email = form.email.data
#         user.save()
#         redirect('register')
#     return render_response('register.html', form=form)


    form = MyForm()
    if request.method == "POST" : 
        return "OK"
    return render_template('init.html', form=form)


@home.route('/run', methods=["GET", "POST"])
def run() : 
    return "hello"