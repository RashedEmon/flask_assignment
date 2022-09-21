#Related third party imports.
from functools import wraps
from flask import request,make_response,jsonify,current_app,abort
import jwt
#Local application specific imports.
from flask_root.data import users

def token_login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        id = kwargs.get('id',None)
        print(id)
        token = None
        if "Authorization" in request.headers:
            scheme,token = request.headers["Authorization"].split(" ")
        if not token:
            return jsonify({
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }), 401
        
        print(token)
        if scheme != 'Bearer':
            return jsonify({
                "message": "Bearer Token is missing!",
                "data": None,
                "error": "Unauthorized"
            })

        try:
            data=jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            print(data)
            temp_user = None
            for user in users:
                if user.username == data["username"]:
                    print(data["username"])
                    temp_user=user
            current_user=temp_user
            if current_user is None:
                return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
            if not current_user.active:
                abort(403)
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return func(*args,**kwargs)
    return wrapper


