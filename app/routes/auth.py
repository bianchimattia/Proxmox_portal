from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from app.models.user import User
from flask_login import login_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            print('Username o password non corretti')
    return render_template('login.html')
