from flask import Flask
from extensions import db
from config import DevConfig, TestConfig
from views.moves import moves_ns
from views.module_one import module_one_ns
from views.module_two import module_two_ns
from views.sparring import sparring_ns
from views.colour import colour_ns
from flask_restx import Api


def create_app(test_config=None):
    """Application factory"""
    app = Flask(__name__)
    if test_config is None:
        app.config.from_object(DevConfig)
    else:
        app.config.from_object(TestConfig)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    api = Api(app)

    api.add_namespace(moves_ns)
    api.add_namespace(module_one_ns)
    api.add_namespace(module_two_ns)
    api.add_namespace(sparring_ns)
    api.add_namespace(colour_ns)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
