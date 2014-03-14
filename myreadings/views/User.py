from flask import Blueprint, render_template, abort, url_for, \
                  request, flash, redirect, session

from myreadings.app  import db
from myreadings.models.User import User
from myreadings.utils import md5

user = Blueprint("user", __name__)

@user.route('/login')
def login():
    return render_template("login.html")

@user.route('/login', methods=['POST'])
def perform_login():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email, password=md5(password)).first()
    if user:
        flash("welcome back!")
        session['status'] = 'logined'
        session['user_id'] = user.id
    else:
        flash("wrong email or password")
    return redirect(url_for('index'))

@user.route('/sign-up')
def register():
    return render_template("register.html")

@user.route('/sign-up', methods=['POST'])
def perform_register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    user = User(username, email, password)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("index"))

@user.route('/logout')
def logout():
    session.pop('status')
    session.pop('user_id')
    return redirect(url_for("index"))