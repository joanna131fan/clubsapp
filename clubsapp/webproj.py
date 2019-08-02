'''
from __future__ import print_function
from flask import redirect, Flask, render_template, url_for, flash
from flask_assets import Bundle, Environment
from flask_login import current_user, login_user, logout_user, login_required
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='97df9c8029f9e716e18088cb1db30e23'
js = Bundle('main.js', 'bootstrap.js',output='gen/all.js')

assets = Environment(app)
assets.register('all.js', js)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/viewminutes")
def viewminutes():
    return render_template('view.html', title='View Minutes')

@app.route("/recordminutes")
def recordminutes():
    return render_template('record.html', title='Record Minutes')

@app.route("/myclubs")
def myclubs():
    return render_template('myclubs.html', title='My Clubs')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
    
'''
