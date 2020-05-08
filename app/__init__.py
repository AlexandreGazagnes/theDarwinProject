from flask import Flask
from flask import render_template, redirect, escape, request, session

from params import Params
from src.algo_child import NathanAlgo

app = Flask(__name__,   template_folder="templates", static_folder='static')






@app.route('/')
def home():

    return render_template('home.html', oject = "Hello")


@app.route('/init', methods=["GET", "POST"])
def init() : 

    if request.method == "GET" : 
        pass
    else : 
        pass

    return ""
