from flask import Blueprint, render_template, session, redirect, url_for
from .models import User, LoginLog

views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def index():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('dashboard.html', user=user)
    return redirect(url_for('auth.login'))

@views_bp.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user = User.query.get(session['user_id'])
    logs = LoginLog.query.filter_by(user_id=user.id).order_by(LoginLog.login_time.desc()).limit(10).all()
    return render_template('profile.html', user=user, login_logs=logs)
