from models import ModuleTwo, Moves
from .moves import moves_dto
from flask_restx import Resource, fields, Namespace
from flask import abort

module_two_ns = Namespace("module_2", description="Namespace for module 2 combinations")

module_two_dto = module_two_ns.model("ModuleTwo", {
    "id": fields.Integer,
    "name": fields.String,
    "code": fields.String,
    "moves": fields.String,
    "is_kick": fields.Boolean,
    "is_jump": fields.Boolean,
    "notes": fields.String
})


@module_two_ns.route("/all")
class CombosAll(Resource):
    @module_two_ns.marshal_list_with(module_two_dto)
    def get(self):
        """Get all combinations"""
        combos = ModuleTwo.query.all()
        return combos


@module_two_ns.route("/id/<int:id>")
class CombosById(Resource):
    @module_two_ns.marshal_with(module_two_dto)
    def get(self, id):
        """Get combination by id"""
        combos = ModuleTwo.query.get_or_404(id)
        return combos


@module_two_ns.route("/code/<string:code>")
class CombosByCode(Resource):
    @module_two_ns.marshal_with(module_two_dto)
    def get(self, code):
        """Get combination by code"""
        combos = ModuleTwo.query.filter_by(code=code).first_or_404()
        return combos


@module_two_ns.route("/combo_moves/<int:id>")
class ComboMovesById(Resource):

    @module_two_ns.marshal_list_with(moves_dto)
    def get(self, id):
        """Get list of moves that appear in the combination"""
        combo_moves = ModuleTwo.query.filter(ModuleTwo.id == id).first_or_404().moves

        if combo_moves is None:
            return abort(404, "No combination moves")

        no_whitespace = combo_moves.replace(" ", "")
        list_moves = no_whitespace.split(",")
        moves = Moves.query.filter(Moves.code.in_(list_moves)).order_by(Moves.id).all()

        return moves


@module_two_ns.route("/combo_moves/<string:code>")
class ComboMovesByCode(Resource):

    @module_two_ns.marshal_list_with(moves_dto)
    def get(self, code):
        """Get list of moves that appear in the combination"""
        combo_moves = ModuleTwo.query.filter(ModuleTwo.code == code).first_or_404().moves

        if combo_moves is None:
            return abort(404, "No combination moves")

        no_whitespace = combo_moves.replace(" ", "")
        list_moves = no_whitespace.split(",")
        moves = Moves.query.filter(Moves.code.in_(list_moves)).order_by(Moves.id).all()

        return moves


@module_two_ns.route("/not_jump_or_kick")
class CombosNotJumpOrKick(Resource):

    @module_two_ns.marshal_list_with(module_two_dto)
    def get(self):
        """Get list of combinations that do not involve kick or jump"""
        combos = ModuleTwo.query.filter(ModuleTwo.is_kick == 0, ModuleTwo.is_jump == 0).all()
        return combos


@module_two_ns.route("/not_jump")
class CombosNotJump(Resource):

    @module_two_ns.marshal_list_with(module_two_dto)
    def get(self):
        """Get list of combinations that do not involve jump"""
        combos = ModuleTwo.query.filter(ModuleTwo.is_jump == 0).all()
        return combos


@module_two_ns.route("/not_kick")
class CombosNotKick(Resource):

    @module_two_ns.marshal_list_with(module_two_dto)
    def get(self):
        """Get list of combinations that do not involve kick"""
        combos = ModuleTwo.query.filter(ModuleTwo.is_kick == 0).all()
        return combos


@module_two_ns.route("/is_kick")
class CombosWithKick(Resource):

    @module_two_ns.marshal_list_with(module_two_dto)
    def get(self):
        """Get list of combinations that involve kick"""
        combos = ModuleTwo.query.filter(ModuleTwo.is_kick == 1).all()
        return combos


@module_two_ns.route("/is_jump")
class CombosWithJump(Resource):

    @module_two_ns.marshal_list_with(module_two_dto)
    def get(self):
        """Get list of combinations that involve jump"""
        combos = ModuleTwo.query.filter(ModuleTwo.is_jump == 1).all()
        return combos


@module_two_ns.route("/is_jump_kick")
class CombosWithJumpKick(Resource):

    @module_two_ns.marshal_list_with(module_two_dto)
    def get(self):
        """Get list of combinations that involve jump kick"""
        combos = ModuleTwo.query.filter(ModuleTwo.is_kick == 1, ModuleTwo.is_jump == 1).all()
        return combos
