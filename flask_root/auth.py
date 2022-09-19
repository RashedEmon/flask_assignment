from crypt import methods
import functools
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('/login', __name__, url_prefix='/')

users = {
    "emon": generate_password_hash("rashed"),
    "basar": generate_password_hash("khademul")
}
basicAuth = HTTPBasicAuth()


@basicAuth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@bp.errorhandler(405)
def error_handler_405(error):
    # return '405 gotta'
    return render_template('templates/errors/404.html')


@bp.route('/login',methods=['GET','POST'])
@basicAuth.login_required
def login():
    return render_template('templates/auth/login.html')