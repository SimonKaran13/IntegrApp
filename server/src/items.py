import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from .auth import is_user_refugee

bp = Blueprint('refugee_items', __name__, url_prefix='/refugee_items')

@bp.route('/', methods=('GET', 'POST'))
def items():
    if request.method == 'POST':
        pass
    
    ## todo: user is refugee or local?

    if is_user_refugee == "1":
        return render_template('refugee_events/refugee_events.html')
    else:
        return render_template('local_events/local_events.html')
        
''' ADDITIONAL NICE TO HAVE PAGE
@bp.route('/shirts', methods=('POST'))
def items_shirts():
    return render_template(TO BE FILLED)
'''