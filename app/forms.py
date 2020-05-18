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


choicesFuncts = [(k, v["expression"]) for k, v in Functs.as_dict.items()]
choicesObjectives = [("min", "Min"), ("max", "Max")]


class InitForm(FlaskForm):

    funct = SelectField(
        "Function",
        choices=choicesFuncts,
        description="jndkzdnejkjdkzndkdzdnzkdnkzdjzd",
        render_kw={"class": "form-control"},
        validators=[DataRequired(message="data required"),],
    )
    objective = SelectField(
        "Objective",
        choices=choicesObjectives,
        description="jndkzdnejkjdkzndkdzdnzkdnkzdjzd",
        render_kw={"class": "form-control"},
        validators=[DataRequired(message="data required"),],
    )
    interval_up = IntegerField(
        "Interval Up",
        description="jndkzdnejkjdkzndkdzdnzkdnkzdjzd",
        render_kw={"class": "form-control", "placeholder": "ex : 100"},
        validators=[
            DataRequired(message="data required"),
            NumberRange(-100, 100, message="please -100 --> 100"),
        ],
    )
    interval_down = IntegerField(
        "Interval Down",
        description="jndkzdnejkjdkzndkdzdnzkdnkzdjzd",
        render_kw={"class": "form-control", "placeholder": "ex : -100"},
        validators=[
            DataRequired(message="data required"),
            NumberRange(-100, 100, message="please -100 --> 100"),
        ],
    )

    seed_parents = IntegerField(
        "Seed Parents",
        render_kw={"class": "form-control", "placeholder": "ex : 100"},
        description="nb of initial parents (between 10 and 1000)",
        validators=[
            DataRequired(message="data required"),
            NumberRange(10, 1000, message="please 10 --> 1000"),
        ],
    )
    kill_rate = FloatField(
        "Kill Rate",
        description="jndkzdnejkjdkzndkdzdnzkdnkzdjzd",
        render_kw={"class": "form-control", "placeholder": "ex : 0.75"},
        validators=[
            DataRequired(message="data required"),
            NumberRange(0.01, 0.99, message="please 0.01 --> 0.99"),
        ],
    )
    average_child_numb = FloatField(
        "% average childs vs mutant child",
        description="jndkzdnejkjdkzndkdzdnzkdnkzdjzd",
        render_kw={"class": "form-control", "placeholder": "ex : 0.25"},
        validators=[
            DataRequired(message="data required"),
            NumberRange(0.01, 0.99, message="please 0.01 --> 0.99"),
        ],
    )
    submit = SubmitField("Go", render_kw={"class": "btn btn-primary form-control"},)

    # def validate_interval(form):
    #     if field.interval_down.data > field.interval_up.data:
    #         raise ValidationError("Down > Up")


class RunForm(FlaskForm):

    years = IntegerField(
        "Years",
        description="nb of years, each year is a cycle of killing, mutating etc.",
        default=1,
        render_kw={"class": "form-control"},
        validators=[
            DataRequired(message="data required"),
            NumberRange(1, 100, message="please 1 --> 100"),
        ],
    )

    speed = IntegerField(
        "Speed",
        description="year per sec (min 1, max 100)",
        default=1,
        render_kw={"class": "form-control"},
        validators=[
            DataRequired(message="data required"),
            NumberRange(1, 100, message="please 1 --> 100"),
        ],
    )
    submit = SubmitField("Run", render_kw={"class": "btn btn-primary form-control"},)
