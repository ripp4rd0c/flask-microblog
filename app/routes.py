from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'mohamad'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm() # create form object
    
    # check if form is submitted, if it is, validate the form and redirect to index page 
    if form.validate_on_submit():
        flash(f"login requested for {form.username.data}\nremember me = {form.remember_me.data}")
        return redirect('/index')

    return render_template('login.html', form=form, title='Sign In')
