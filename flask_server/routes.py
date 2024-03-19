from flask import current_app
from app import create_app
from extensions import db
from models import Moves

app = create_app()


@app.route("/")
def home():
    return {"message": "hello"}


if __name__ == "__main__":
    app.run(debug=True)
