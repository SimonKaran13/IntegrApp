import functools

from flask import (
    Blueprint, render_template
)

bp = Blueprint('homepage', __name__)

@bp.route('/')
def homepage():
    return render_template("homepage/Homepage.html")