from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired

class UserDataForm(FlaskForm):
    weight = IntegerField('Weight', validators = [DataRequired()]) 
    activityLevel = SelectField('Recent Activity Level', validators=[DataRequired()],
                                choices=[('Not Active', 'Not Active'),
                                        ('Lighly Active', 'Lightly Active'),
                                        ('Moderately Active', 'Moderately Active'),
                                        ('Very Active ', 'Very Active')])                
    submit = SubmitField('Update Fitness Progress')









