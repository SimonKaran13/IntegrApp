import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'IntegrApp running on flask'

    from . import db
    db.init_app(app)

    # authentication
    from . import auth
    app.register_blueprint(auth.bp)

    # forum
    from . import forum
    app.register_blueprint(forum.bp)
    
    from . import events
    app.register_blueprint(events.bp)

    from . import courses
    app.register_blueprint(courses.bp)

    from . import homepage
    app.register_blueprint(homepage.bp)

    return app
