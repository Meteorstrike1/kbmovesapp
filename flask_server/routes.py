from flask import current_app
from app import create_app
from extensions import db
from models import Moves
from flask_restx import Api, Resource, fields

app = create_app()
api = Api(app)

moves_dto = api.model("Moves", {
    "id": fields.Integer,
    "name": fields.String,
    "code": fields.String,
    "belt_colour": fields.String,
    "lesson_plan": fields.Integer,
    "related_moves": fields.String,
    "module_combo": fields.String,
    "is_defence": fields.String,
    "is_kick": fields.Boolean,
    "is_jump": fields.Boolean,
    "notes": fields.String
})


@app.route("/")
def home():
    return {"message": "hello"}


@api.route("/moves")
class MovesAll(Resource):
    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get all moves"""
        moves = Moves.query.all()
        return moves


@api.route("/moves/belt/<string:colour>")
class MovesByColour(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self, colour):
        """Get moves by belt colour"""
        moves = Moves.query.filter(Moves.belt_colour == colour).all()
        return moves


@api.route("/moves/name/<string:name>")
class MovesByName(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self, name):
        """Get moves by name"""
        moves = Moves.query.filter(Moves.name.ilike(f"%{name}%")).all()
        return moves


@api.route("/moves/hand_defences/graded")
class HandDefencesGraded(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get list of slide and step back hand defences"""
        moves = Moves.query.filter(Moves.is_defence == "hand", Moves.id < 129).all()
        return moves


@api.route("/moves/leg_defences/all")
class LegDefencesAll(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get list of all leg defences"""
        moves = Moves.query.filter(Moves.is_defence == "leg").all()
        return moves


@api.route("/moves/hand_defences/all")
class HandDefencesAll(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get list of all hand defences"""
        moves = Moves.query.filter(Moves.is_defence == "hand").all()
        return moves


@api.route("/moves/in_module_1")
class Module1Moves(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get list of all moves/related moves that appear in module 1"""
        moves = Moves.query.filter(Moves.module_combo != "NULL", Moves.id < 88).all()
        return moves


@api.route("/moves/in_module_2")
class Module2Moves(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get list of all moves/related moves that appear in module 2"""
        moves = Moves.query.filter(Moves.module_combo != "NULL", Moves.id > 88).all()
        return moves


@api.route("/moves/not_module_1")
class MovesNotinModule1(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get list of all moves that do not appear in module 1"""
        moves = Moves.query.filter(Moves.module_combo.is_(None), Moves.id < 88).all()
        return moves


@api.route("/moves/not_module_2")
class MovesNotinModule2(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get list of all moves that do not appear in module 2"""
        moves = Moves.query.filter(Moves.module_combo.is_(None), Moves.id > 88).all()
        return moves


@api.route("/moves/not_jump_or_kick")
class MovesNotJumpOrKick(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get list of moves that do not involve kick or jump"""
        moves = Moves.query.filter(Moves.is_kick == 0, Moves.is_jump == 0).all()
        return moves


@api.route("/moves/not_jump")
class MovesNotJump(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get list of moves that do not involve jump"""
        moves = Moves.query.filter(Moves.is_jump == 0).all()
        return moves


@api.route("/moves/not_kick")
class MovesNotKick(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get list of moves that do not involve kick"""
        moves = Moves.query.filter(Moves.is_kick == 0).all()
        return moves


@api.route("/moves/is_kick")
class MovesWithKick(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get list of moves that involve kick"""
        moves = Moves.query.filter(Moves.is_kick == 1).all()
        return moves


@api.route("/moves/is_jump")
class MovesWithJump(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get list of moves that involve jump"""
        moves = Moves.query.filter(Moves.is_jump == 1).all()
        return moves


@api.route("/moves/is_jump_kick")
class MovesWithJumpKick(Resource):

    @api.marshal_list_with(moves_dto)
    def get(self):
        """Get list of moves that involve jump kick"""
        moves = Moves.query.filter(Moves.is_kick == 1, Moves.is_jump == 1).all()
        return moves


if __name__ == "__main__":
    app.run(debug=True)
