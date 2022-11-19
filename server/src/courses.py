import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from .auth import is_user_refugee

bp = Blueprint('courses', __name__, url_prefix='/courses')

@bp.route('/', methods=('GET', 'POST'))
def items():
    if request.method == 'POST':
        pass
    
    ## todo: user is refugee or local?

    if is_user_refugee == "1":
        return render_template('refugee_courses/refugee_courses.html')
    else:
        return render_template('local_courses/local_courses.html')
        
''' ADDITIONAL NICE TO HAVE PAGE
@bp.route('/a_course', methods=('POST'))
def items_shirts():
    return render_template(a course html)
'''