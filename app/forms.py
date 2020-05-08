from flask_wtf import FlaskForm
from wtforms import (Form, BooleanField, StringField, validators, SelectField, IntegerField,SelectMultipleField, FloatField, SubmitField)
from wtforms.validators import DataRequired, Length


class MyForm(Form  ):
    first_name = StringField(u'First Name', validators=[validators.input_required()])
    last_name  = StringField(u'Last Name', validators=[validators.optional()])

    funct = SelectField("Function", choices=[(0, "funct0"), (1, "Funct1")])
    objective = SelectField("Function", choices=[(0, "min"), (1, "max")])
    interval_up = IntegerField("Interval Up")
    interval_down = IntegerField("Interval Down")
    seed_parents = IntegerField("Interval Down")
    kill_rate = FloatField("Kill Rate")
    average_child_numb = FloatField("% average childs")
    submit = SubmitField('Go')