from flask import (
    Flask,
    escape,
    request,
    flash,
    url_for,
    render_template,
    abort,
    redirect,
)

# from flask import session, Session
#
# from flask_sqlalchemy import SQLAlchemy
# # from flask.ext.session import Session
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager, UserMixin
# from flask_mail import Mail
from flask import Blueprint
from app.forms import InitForm, RunForm

from app import ALGO

from src.functs import Functs
from src import EvolutionAlgo1D


home = Blueprint("home", __name__)


@home.route("/")
def welcome():

    return render_template("home.html", object=ALGO)


@home.route("/init", methods=["GET", "POST"])
def init():

    form = InitForm(request.form)

    feats = [
        "funct",
        "objective",
        "interval_up",
        "interval_down",
        "seed_parents",
        "kill_rate",
        "average_child_numb",
    ]
    for f in feats:
        _val = getattr(form, f).data
        print(f"{f} : {type(_val)} is {_val} ")

    print(request.method)

    if request.method == "POST":
        global ALGO
        ALGO = EvolutionAlgo1D(
            funct=Functs.as_dict[form.funct.data],
            objective=form.objective.data,
            interval=[form.interval_down.data, form.interval_up.data],
            seed_parents=form.seed_parents.data,
            kill_rate=form.kill_rate.data,
            average_child_numb=form.average_child_numb.data,
        )
        print(ALGO)
        # if form.validate():
        #     redirect(url_for("home.run"))
        # else:
        #     print("Error")
        return redirect(url_for("home.run"))

    return render_template("init.html", form=form)


@home.route("/run", methods=["GET", "POST"])
def run():

    form = RunForm(request.form)
    global ALGO
    print(ALGO)

    if request.method == "POST":
        ALGO.run(1)
        ALGO.plot_population()
        ALGO.plot_learning()
        return redirect(url_for("home.run"))

    algo = str(ALGO)
    pop = str(ALGO.current_population[:10])
    learning_image = ALGO.learning_images[-1].replace("app/", "")
    population_image = ALGO.population_images[-1].replace("app/", "")
    return render_template(
        "run.html",
        algo=algo,
        pop=pop,
        form=form,
        learning_image=learning_image,
        population_image=population_image,
    )
