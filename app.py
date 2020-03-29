# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

"""

from flask import Flask
from flask_migrate import Migrate

from utils.db_mysql import db

from modules.weather import weather_site, init_app as init_weather_app


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    with app.app_context():
        app.register_blueprint(weather_site)
        init_weather_app(app)
        # Migrate(app, db)
        return app


app = create_app()

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True, port=8080, host="0.0.0.0")
