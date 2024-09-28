from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@main.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        new_user = User(name=name, email=email)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
            return redirect(url_for('main.index'))
        except:
            db.session.rollback()
            flash('Error adding user!', 'danger')
    return render_template('add_user.html')

@main.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        try:
            db.session.commit()
            flash('User updated successfully!', 'success')
            return redirect(url_for('main.index'))
        except:
            db.session.rollback()
            flash('Error updating user!', 'danger')
    return render_template('update_user.html', user=user)

@main.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully!', 'success')
    except:
        db.session.rollback()
        flash('Error deleting user!', 'danger')
    return redirect(url_for('main.index'))
