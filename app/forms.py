from flask_wtf import FlaskForm
from wtforms import (
    Form,
    BooleanField,
    StringField,
    validators,
    SelectField,
    IntegerField,
    SelectMultipleField,
    FloatField,
    SubmitField,
)
from wtforms.validators import DataRequired, Length, NumberRange


from src.functs import Functs

choicesFuncts = [
    ("x2", "x2 (1D)"),
    ("sinFucker", "sinFucker (1D)"),
    ("nathanCos", "nathanCos (1D)"),
]

choicesObjectives = [("min", "Min"), ("max", "Max")]


class InitForm(FlaskForm):

    funct = SelectField(
        "Function",
        choices=choicesFuncts,
        validators=[DataRequired(message="data required"),],
    )
    objective = SelectField(
        "Objective",
        choices=choicesObjectives,
        validators=[DataRequired(message="data required"),],
    )
    interval_up = IntegerField(
        "Interval Up",
        validators=[
            DataRequired(message="data required"),
            NumberRange(-100, 100, message="please -100 --> 100"),
        ],
    )
    interval_down = IntegerField(
        "Interval Down",
        validators=[
            DataRequired(message="data required"),
            NumberRange(-100, 100, message="please -100 --> 100"),
        ],
    )

    seed_parents = IntegerField(
        "Seed Parents",
        description="nb of initial parents (between 10 and 1000)",
        validators=[
            DataRequired(message="data required"),
            NumberRange(10, 1000, message="please 10 --> 1000"),
        ],
    )
    kill_rate = FloatField(
        "Kill Rate",
        validators=[
            DataRequired(message="data required"),
            NumberRange(0.01, 0.99, message="please 0.01 --> 0.99"),
        ],
    )
    average_child_numb = FloatField(
        "% average childs",
        validators=[
            DataRequired(message="data required"),
            NumberRange(0.01, 0.99, message="please 0.01 --> 0.99"),
        ],
    )
    submit = SubmitField("Go")

    # def validate_interval(form):
    #     if field.interval_down.data > field.interval_up.data:
    #         raise ValidationError("Down > Up")


class RunForm(FlaskForm):

    n = IntegerField(
        "n",
        description="nb of run",
        default=1,
        validators=[
            DataRequired(message="data required"),
            NumberRange(1, 100, message="please 10 --> 1000"),
        ],
    )
    submit = SubmitField("run")