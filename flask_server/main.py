from flask import Flask
from extensions import db
from config import DevConfig, TestConfig


def create_app(test_config=None):
    """Application factory"""
    app = Flask(__name__)
    if test_config is None:
        app.config.from_object(DevConfig)
    else:
        app.config.from_object(TestConfig)

    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
