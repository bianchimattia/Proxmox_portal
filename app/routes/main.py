# app/routes/main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required  
def home():
    return render_template('dashboard.html', user=current_user)


@main_bp.route('/creazione')
@login_required  
def creazione():
    return render_template('creazione.html', user=current_user)


@main_bp.route('/lista')
@login_required  
def lista():
    return render_template('lista.html', user=current_user)