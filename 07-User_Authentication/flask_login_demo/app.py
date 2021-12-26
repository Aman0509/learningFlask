from flask_login_demo import db, app
from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, login_user, logout_user
from flask_login_demo.models import User
from flask_login_demo.forms import LoginForm, RegistrationForm


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('user.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            # login_user was imported from flask_login
            login_user(user)
            flash('Logged in successfully.')

            # If user is trying to access a page that requires login, we will first save that request and redirect them
            # to login page.
            next = request.args.get('next')
            if next is None or not next[0] == '/':
                next = url_for('welcome_user')
            return redirect(next)

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # logout_user was imported from flask_login
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)