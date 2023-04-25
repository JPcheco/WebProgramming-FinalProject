from jsonpickle import encode
from flask import Flask
from jinja2 import Environment
from flask import abort, redirect, url_for
from flask import request
from flask import render_template
from flask import session
from builtins import enumerate
from userdao import UserDao
from user import User
import logging 

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
env = Environment()
env.globals.update(enumerate=enumerate)

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('greetscreen'))

@app.route('/greetscreen',  methods = ['GET', 'POST'])
def greetscreen():
    return render_template('greetscreen.html', **locals())

@app.route('/login',  methods=['GET', 'POST'])
def login():
    userid = request.form.get('userid', None)
    password = request.form.get('password', None)
    if (isValid(userid, password)):
        session['userid'] = userid
        return redirect(url_for('homepage'))
    else:
        return render_template('login.html', **locals())

@app.route('/homepage',  methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')

@app.route('/signup',  methods=['GET', 'POST'])
def signup():
    dao = UserDao()
    new_userid = request.form.get('new_userid')
    new_password = request.form.get('new_password')

    if ((new_userid is not None) and (new_password is not None)):
        dao.insert(new_userid, new_password)
        return redirect(url_for('login'))
    else:
        return render_template('signup.html', **locals())

@app.route('/create',  methods=['GET', 'POST'])
def create():
    return render_template('create.html')

@app.route('/search',  methods=['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route('/bookmark',  methods=['GET', 'POST'])
def bookmark():
    return render_template('bookmark.html')

def isValid(userid, password):
    dao = UserDao()
    user = dao.selectByUserId(userid)

    if (user is not None) and (user.userid == userid) and (user.password == password):
        session['user'] = encode(user)
        return True
    else:
        return False

if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)


