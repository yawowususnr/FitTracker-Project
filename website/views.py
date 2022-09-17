from ast import If
from flask import Blueprint, render_template, flash, redirect, url_for, get_flashed_messages
from flask.helpers import flash
from flask.scaffold import _endpoint_from_view_func
from flask_login import login_required, logout_user, current_user
from flask_wtf import form
from sqlalchemy.orm import dynamic_loader
from website import form2
from website.form import UserDataForm
from website.form2 import UserGoalForm
from website.models import IncomeExpenses
from website.models import UserGoal
from website import db
import json

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    entries = IncomeExpenses.query.order_by(IncomeExpenses.date.desc()).all()
    msg = Message(subject="Activity Report", sender='owusu_ys@soshgic.edu', receipts=['yawsnr33@gmail.com'])
    mail.send(msg)
    return render_template('home.html', user=current_user, entries = entries)

@views.route('/splash')
@login_required
def splash():
    return render_template('splash.html', user=current_user)

@views.route('/goal', methods = ['GET', 'POST'])
@login_required
def goal():
    form = UserGoalForm()
    if form.validate_on_submit():
        entry = UserGoal(weight=form.weight.data, weight_goal=form.weight_goal.data, gender=form.gender.data, height=form.height.data, age=form.age.data)
        db.session.add(entry)
        db.session.commit()
        flash("Successful Entry!", 'success')
        return redirect(url_for('views.home'))
    return render_template('goal.html', form=form, user=current_user)


@views.route('/add', methods = ['GET', 'POST'])
@login_required
def add():
    form = UserDataForm()
    if form.validate_on_submit():
        entry = IncomeExpenses(weight=form.weight.data, activityLevel=form.activityLevel.data)
        db.session.add(entry)
        db.session.commit()
        flash("Successful Entry!", 'success')
        return redirect(url_for('views.home'))
    return render_template("add.html", form = form, user=current_user)


@views.route('/delete/<int:entry_id>')
@login_required
def delete(entry_id):
    entry = IncomeExpenses.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for("views.home"))


@views.route('/dashboard')
@login_required
def dashboard():
    income_vs_expense = db.session.query(db.func.sum(IncomeExpenses.weight), IncomeExpenses.weight).group_by(IncomeExpenses.weight).order_by(IncomeExpenses.weight).all()

    dates = db.session.query(db.func.sum(IncomeExpenses.weight), IncomeExpenses.date).group_by(IncomeExpenses.date).order_by(IncomeExpenses.date).all()

    entries = IncomeExpenses.query.order_by(IncomeExpenses.date.desc()).all()
    currentWeight = entries[0].weight
    currentActivity = entries[0].activityLevel

    

    goal_info = UserGoal.query.order_by(UserGoal.date.desc()).all()
    goalweight = goal_info[0].weight_goal

    gender = goal_info[0].gender
    bmr = 0
    

    height = goal_info[0].height
    bmi = int(currentWeight/((height/100)*(height/100)))


    age=goal_info[0].age

    bmr = int(66.47 + (13.75 * currentWeight) + (5.003 * (height)) - (6.755 * age))

    calInt = 0
    for i in range(1):
        if currentActivity == "Not Active":
            calInt = int(bmr * 1.2)
        elif currentActivity == "Lightly Active":
            calInt = int(bmr * 1.375)
        elif currentActivity == "Moderately Active":
            calInt = int(bmr * 1.5)
        elif currentActivity == "Very Active":
            calInt = int(bmr * 1.75)

    print(bmr)
    print(calInt)
    print(currentActivity)

    consume = 0

    if currentWeight > goalweight:
      consume = (calInt - 300)
    elif currentWeight == goalweight:
     consume = (calInt - 0)
    else:
        consume = (calInt + 300)

    income_expense = []
    for total_weight, _ in income_vs_expense:
        income_expense.append(total_weight)

    over_time_expenditure = []
    dates_labels = []
    for weight, date in dates:
        over_time_expenditure.append(weight)
        dates_labels.append(date.strftime('%m-%d-%y'))

    return render_template('dashboard.html', user=current_user, calInt=calInt, entries = entries, currentWeight = currentWeight, goalweight = goalweight, bmi = bmi, consume = consume, gender = gender, bmr = bmr,
        income_vs_expenses = json.dumps(income_expense),
        over_time_expenditure = json.dumps(over_time_expenditure),
        dates_label = json.dumps(dates_labels)
    )

@views.route('/index')
def index():
    return render_template('index.html', user=current_user)


