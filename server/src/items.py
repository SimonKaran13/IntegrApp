import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('refugee_items', __name__, url_prefix='/refugee_items')

@bp.route('/', methods=('GET', 'POST'))
def items():
    if request.method == 'POST':
        pass
    
    ## todo: user is refugee or local?
    return render_template('auth/register.html')

''' ADDITIONAL NICE TO HAVE PAGE
@bp.route('/shirts', methods=('POST'))
def items_shirts():
    return render_template(TO BE FILLED)
'''