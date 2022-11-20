import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from .auth import is_user_refugee, login_required

bp = Blueprint('items', __name__, url_prefix='/items')

@bp.route('/', methods=('GET', 'POST'))
@login_required
def items():
    if request.method == 'POST':
        pass
    
    print(type(is_user_refugee()))
    ## todo: user is refugee or local?
    if is_user_refugee() == "1":
        return render_template('refugee_items/refugee_items.html')
    else:
        return render_template('local_items/local_items.html')
        
''' ADDITIONAL NICE TO HAVE PAGE
@bp.route('/shirts', methods=('POST'))
def items_shirts():
    return render_template(TO BE FILLED)
'''