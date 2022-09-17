from . import db
from flask_login import UserMixin
from sqlalchemy import func
from datetime import datetime
import random

class IncomeExpenses(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    weight = db.Column(db.Integer, nullable=False)
    activityLevel = db.Column(db.String(30), nullable=False, default='Not Active')


class UserGoal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    weight_goal = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(30), nullable=False, default='male')


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    "https://www.active.com/fitness/calculators/nutrition"