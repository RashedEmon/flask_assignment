#Related third party imports.
from flask_httpauth import HTTPDigestAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_login import login_required
#Local application specific imports.
from flask_root.data import todos



post_bp = Blueprint('/post', __name__, url_prefix='/')

digestAuth = HTTPDigestAuth()
tokenAuth = HTTPTokenAuth(scheme='Bearar')

@post_bp.route('posts/',methods=['GET'])
@login_required
def posts():
    return todos

@post_bp.route('post/<id>',methods=['GET'])
def postById(id):
    print(type(id))
    for todo in todos:
        if todo['id'] == id:
            return todo

    return 'Not Found', 404

