from flask import Flask

from potboiler import __version__, config
from potboiler.flask.blueprints import cache


def create_app(debug=False):

    app = Flask('potboiler', static_folder='flask/static', template_folder='flask/templates')
    app.config.from_object(config.flask)
    cache.init_app(app, config={'CACHE_TYPE': 'simple'})

    if debug:
        from werkzeug.debug import DebuggedApplication
        app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

    import potboiler.flask.blueprints.web

    app.register_blueprint(potboiler.flask.blueprints.web.bp, url_prefix='/')

    app.add_template_global(lambda: __version__, name='app_version')
    return app
