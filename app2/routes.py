from app2 import app
from flask import render_template, flash, redirect, url_for
from app2.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user1 = {'username' : 'jayden'}
    info = [
        {'email': 'hello', 'age': 'zxc'},
        {'email': 'hello2', 'age': 'zxc2'}
    ]
    return render_template('index.html',title = 'home',user=user1,info=info)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('{} login success!!'.format(form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html',form=form)
