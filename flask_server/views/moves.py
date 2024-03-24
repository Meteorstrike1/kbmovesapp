from models import Moves
from flask_restx import Resource, fields, Namespace
from flask import abort


moves_ns = Namespace("moves", description="Namespace for individual moves")

moves_dto = moves_ns.model("Moves", {
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


@moves_ns.route("/all")
class MovesAll(Resource):
    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get all moves"""
        moves = Moves.query.all()
        return moves


@moves_ns.route("/id/<int:id>")
class MovesById(Resource):
    @moves_ns.marshal_with(moves_dto)
    def get(self, id):
        """Get move by id"""
        moves = Moves.query.get_or_404(id)
        return moves


@moves_ns.route("/code/<string:code>")
class MovesByCode(Resource):
    @moves_ns.marshal_with(moves_dto)
    def get(self, code):
        """Get move by code"""
        moves = Moves.query.filter_by(code=code).first_or_404()
        return moves


@moves_ns.route("/belt/<string:colour>")
class MovesByColour(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self, colour):
        """Get moves by belt colour"""
        moves = Moves.query.filter(Moves.belt_colour == colour).all()
        return moves


@moves_ns.route("/name/<string:name>")
class MovesByName(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self, name):
        """Get moves by name"""
        moves = Moves.query.filter(Moves.name.ilike(f"%{name}%")).all()
        if len(moves) == 0:
            return abort(404, "No moves found")
        return moves


@moves_ns.route("/hand_defences/graded")
class HandDefencesGraded(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get list of slide and step back hand defences"""
        moves = Moves.query.filter(Moves.is_defence == "hand", Moves.id < 129).all()
        return moves


@moves_ns.route("/leg_defences/all")
class LegDefencesAll(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get list of all leg defences"""
        moves = Moves.query.filter(Moves.is_defence == "leg").all()
        return moves


@moves_ns.route("/hand_defences/all")
class HandDefencesAll(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get list of all hand defences"""
        moves = Moves.query.filter(Moves.is_defence == "hand").all()
        return moves


@moves_ns.route("/in_module_1")
class Module1Moves(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get list of all moves/related moves that appear in module 1"""
        moves = Moves.query.filter(Moves.module_combo != "NULL", Moves.id < 88).all()
        return moves


@moves_ns.route("/in_module_2")
class Module2Moves(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get list of all moves/related moves that appear in module 2"""
        moves = Moves.query.filter(Moves.module_combo != "NULL", Moves.id > 88).all()
        return moves


@moves_ns.route("/not_module_1")
class MovesNotinModule1(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get list of all moves that do not appear in module 1"""
        moves = Moves.query.filter(Moves.module_combo.is_(None), Moves.id < 88).all()
        return moves


@moves_ns.route("/not_module_2")
class MovesNotinModule2(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get list of all moves that do not appear in module 2"""
        moves = Moves.query.filter(Moves.module_combo.is_(None), Moves.id > 88).all()
        return moves


@moves_ns.route("/not_jump_or_kick")
class MovesNotJumpOrKick(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get list of moves that do not involve kick or jump"""
        moves = Moves.query.filter(Moves.is_kick == 0, Moves.is_jump == 0).all()
        return moves


@moves_ns.route("/not_jump")
class MovesNotJump(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get list of moves that do not involve jump"""
        moves = Moves.query.filter(Moves.is_jump == 0).all()
        return moves


@moves_ns.route("/not_kick")
class MovesNotKick(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get list of moves that do not involve kick"""
        moves = Moves.query.filter(Moves.is_kick == 0).all()
        return moves


@moves_ns.route("/is_kick")
class MovesWithKick(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get list of moves that involve kick"""
        moves = Moves.query.filter(Moves.is_kick == 1).all()
        return moves


@moves_ns.route("/is_jump")
class MovesWithJump(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get list of moves that involve jump"""
        moves = Moves.query.filter(Moves.is_jump == 1).all()
        return moves


@moves_ns.route("/is_jump_kick")
class MovesWithJumpKick(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self):
        """Get list of moves that involve jump kick"""
        moves = Moves.query.filter(Moves.is_kick == 1, Moves.is_jump == 1).all()
        return moves


@moves_ns.route("/related_moves/<int:id>")
class RelatedMovesById(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self, id):
        """Get list of related moves"""
        related_moves = Moves.query.filter(Moves.id == id).first().related_moves

        if related_moves is None:
            return abort(404, "No related moves")

        no_whitespace = related_moves.replace(" ", "")
        list_moves = no_whitespace.split(",")
        moves = Moves.query.filter(Moves.code.in_(list_moves)).order_by(Moves.id).all()

        return moves


@moves_ns.route("/related_moves/<string:code>")
class RelatedMovesByCode(Resource):

    @moves_ns.marshal_list_with(moves_dto)
    def get(self, code):
        """Get list of related moves"""
        related_moves = Moves.query.filter(Moves.code == code).first().related_moves

        if related_moves is None:
            return abort(404, "No related moves")

        no_whitespace = related_moves.replace(" ", "")
        list_moves = no_whitespace.split(",")
        moves = Moves.query.filter(Moves.code.in_(list_moves)).order_by(Moves.id).all()

        return moves

