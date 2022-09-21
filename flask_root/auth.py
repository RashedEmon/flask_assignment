#Standard library imports.
#Related third party imports.
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Blueprint, flash, g, redirect, render_template, request, make_response, session, url_for,current_app
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager,login_user,login_required,current_user,logout_user
import jwt
#Local application specific imports.
from flask_root.data import users,basicAuthUsers
#create a login manager instance
login_manager = LoginManager()


#create blue print
bp = Blueprint('/login', __name__, url_prefix='/')



#create basic auth instance
basicAuth = HTTPBasicAuth()

#this function will automatically verify password where login required decorator used
@basicAuth.verify_password
def verify_password(username, password):
    if username in basicAuthUsers and \
            check_password_hash(basicAuthUsers.get(username), password):
        return username

#this function act as a error 404 handler
@bp.errorhandler(404)
def error_handler_404(error):
    # return '405 gotta'
    return render_template('errors/404.html')


#define user loader
@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.username == user_id:
            return user

#this function handle authentication
@bp.route('/login',methods=['GET','POST'])
@basicAuth.login_required
def login():
    if request.method == 'POST':
        username= request.form['username']
        password = request.form['password']
        user_obj=None
        for user in users:
            # print(user.username)
            if user.username == username:
                user_obj=user
                break
        if user_obj and check_password_hash(user_obj.password,password):
            try:
                user_obj.authenticated=True
                login_user(user_obj)
                token=jwt.encode(
                    {'username': user_obj.username},
                    key=current_app.config['SECRET_KEY'],
                    algorithm="HS256"
                )
                resp=make_response(redirect(url_for('/user/dashboard.dashboard')),)
                resp.set_cookie('token',token)
                return resp
            except Exception:
                pass
                
        else:
            response = make_response(redirect(url_for('/login.login')))
            response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response.headers['Pragma'] = 'no-cache'
            return response

    if request.method == 'GET':
        curr_user = current_user
        try:
            if curr_user.authenticated:
                return redirect(url_for('/user/dashboard.dashboard'))
        except AttributeError:
            pass
        response = make_response(render_template('auth/login.html'))
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        return response

@bp.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    logout_user()
    return render_template('auth/login.html')

