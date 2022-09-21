#Related third party imports.
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Blueprint, flash, g, redirect, render_template, request, make_response, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_required
#Local application specific imports.
from flask_root.data import todos

dashboardbp = Blueprint('/user/dashboard', __name__, url_prefix='/')



@dashboardbp.route('/user/dashboard', methods=['GET'])
@login_required
def dashboard():

    return render_template('dashboard/dashboard.html',todos=todos)