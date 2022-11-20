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

    from blueprints.db import init_app
    init_app(app)

    # authentication
    from blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    # forum
    from blueprints.forum import bp as forum_bp
    app.register_blueprint(forum_bp)
    
    from blueprints.events import bp as events_bp
    app.register_blueprint(events_bp)

    from blueprints.courses import bp as courses_bp
    app.register_blueprint(courses_bp)

    from blueprints.homepage import bp as homepage_bp
    app.register_blueprint(homepage_bp)

    from blueprints.items import bp as items_bp
    app.register_blueprint(items_bp)

    return app
