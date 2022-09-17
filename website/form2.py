from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired

class UserGoalForm(FlaskForm):
    gender = SelectField('Gender', validators=[DataRequired()],
                                choices=[('Male', 'Male'),
                                        ('Female', 'Female')])
    age = IntegerField('Enter Age', validators = [DataRequired()])
    weight = IntegerField('What Is Your Current Weight in KG', validators = [DataRequired()])
    weight_goal = IntegerField('What Is Your Weight Goal', validators = [DataRequired()])   
    height = IntegerField('Enter Height in Centimeters', validators = [DataRequired()])                
    submit = SubmitField('Set Information')








