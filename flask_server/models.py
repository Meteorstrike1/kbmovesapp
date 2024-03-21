from extensions import db


class Moves(db.Model):
    __tablename__ = "moves"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    belt_colour = db.Column(db.String(15), nullable=False)
    lesson_plan = db.Column(db.Integer, nullable=False)
    related_moves = db.Column(db.String(50))
    module_combo = db.Column(db.String(50))
    is_defence = db.Column(db.String(10))
    is_kick = db.Column(db.Boolean, server_default="0")
    is_jump = db.Column(db.Boolean, server_default="0")
    notes = db.Column(db.String(200))

