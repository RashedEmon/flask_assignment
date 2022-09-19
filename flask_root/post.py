from flask_httpauth import HTTPDigestAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

todos = [
        {
        'id': '1',
        'title': 'Learn python'
        },
        {
        'id': '2',
        'title': 'Learn Nodejs'
        },
        {
        'id': '3',
        'title': 'Learn Flask'
        },

    ]

post_bp = Blueprint('/post', __name__, url_prefix='/')

digestAuth = HTTPDigestAuth()
tokenAuth = HTTPTokenAuth(scheme='Bearar')

@post_bp.route('post/',methods=['GET'])
def posts():
    return todos

@post_bp.route('post/<id>',methods=['GET'])
def postById(id):
    print(type(id))
    for todo in todos:
        if todo['id'] == id:
            return todo

    return 'Not Found', 404

