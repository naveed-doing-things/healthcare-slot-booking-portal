from flask import Flask
from .routes import main_bp
import os
import logging
from logging.handlers import RotatingFileHandler
from config import TEMPLATE_DIR, STATIC_DIR, SECRET_KEY, LOG_DIR

def create_app():
    app = Flask(
        __name__,
        template_folder=TEMPLATE_DIR,
        static_folder=STATIC_DIR
    )

    app.config["SECRET_KEY"] = SECRET_KEY

    # ---------- Logging Setup ----------
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    log_file = os.path.join(LOG_DIR, "app.log")

    handler = RotatingFileHandler(log_file, maxBytes=1024000, backupCount=3)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s"
    )
    handler.setFormatter(formatter)

    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.logger.propagate = False
    # -----------------------------------

    app.register_blueprint(main_bp)
    app.logger.info("Flask application initialized")

    return app
