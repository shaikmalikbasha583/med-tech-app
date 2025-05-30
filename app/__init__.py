import logging

from flask import Flask, render_template

from app.data.branches import data
from app.utils import constants as c
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route("/")
    def index():
        logging.info("Returning Home Page")
        return render_template("index.html", data=data, c=c)

    # db.init_app(app)
    # login_manager.init_app(app)

    return app
