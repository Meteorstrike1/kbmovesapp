from models import ModuleOne, Moves
from .moves import moves_dto
from flask_restx import Resource, fields, Namespace
from flask import abort

module_one_ns = Namespace("module_1", description="Namespace for module 1 combinations")

module_one_dto = module_one_ns.model("ModuleOne", {
    "id": fields.Integer,
    "name": fields.String,
    "code": fields.String,
    "moves": fields.String,
    "is_kick": fields.Boolean,
    "is_jump": fields.Boolean,
    "notes": fields.String
})


@module_one_ns.route("/all")
class CombosAll(Resource):
    @module_one_ns.marshal_list_with(module_one_dto)
    def get(self):
        """Get all combinations"""
        combos = ModuleOne.query.all()
        return combos


@module_one_ns.route("/id/<int:id>")
class CombosById(Resource):
    @module_one_ns.marshal_with(module_one_dto)
    def get(self, id):
        """Get combination by id"""
        combos = ModuleOne.query.get_or_404(id)
        return combos


@module_one_ns.route("/code/<string:code>")
class CombosByCode(Resource):
    @module_one_ns.marshal_with(module_one_dto)
    def get(self, code):
        """Get combination by code"""
        combos = ModuleOne.query.filter_by(code=code).first_or_404()
        return combos


@module_one_ns.route("/combo_moves/<int:id>")
class ComboMovesById(Resource):

    @module_one_ns.marshal_list_with(moves_dto)
    def get(self, id):
        """Get list of moves that appear in the combination"""
        combo_moves = ModuleOne.query.filter(ModuleOne.id == id).first_or_404().moves

        if combo_moves is None:
            return abort(404, "No combination moves")

        no_whitespace = combo_moves.replace(" ", "")
        list_moves = no_whitespace.split(",")
        moves = Moves.query.filter(Moves.code.in_(list_moves)).order_by(Moves.id).all()
        if len(moves) == 0:
            return abort(404, "Combination moves could not be found")

        return moves


@module_one_ns.route("/combo_moves/<string:code>")
class ComboMovesByCode(Resource):

    @module_one_ns.marshal_list_with(moves_dto)
    def get(self, code):
        """Get list of moves that appear in the combination"""
        combo_moves = ModuleOne.query.filter(ModuleOne.code == code).first_or_404().moves

        if combo_moves is None:
            return abort(404, "No combination moves")

        no_whitespace = combo_moves.replace(" ", "")
        list_moves = no_whitespace.split(",")
        moves = Moves.query.filter(Moves.code.in_(list_moves)).order_by(Moves.id).all()
        if len(moves) == 0:
            return abort(404, "Combination moves could not be found")

        return moves


@module_one_ns.route("/not_jump_or_kick")
class CombosNotJumpOrKick(Resource):

    @module_one_ns.marshal_list_with(module_one_dto)
    def get(self):
        """Get list of combinations that do not involve kick or jump"""
        combos = ModuleOne.query.filter(ModuleOne.is_kick == 0, ModuleOne.is_jump == 0).all()
        return combos


@module_one_ns.route("/not_jump")
class CombosNotJump(Resource):

    @module_one_ns.marshal_list_with(module_one_dto)
    def get(self):
        """Get list of combinations that do not involve jump"""
        combos = ModuleOne.query.filter(ModuleOne.is_jump == 0).all()
        return combos


@module_one_ns.route("/not_kick")
class CombosNotKick(Resource):

    @module_one_ns.marshal_list_with(module_one_dto)
    def get(self):
        """Get list of combinations that do not involve kick"""
        combos = ModuleOne.query.filter(ModuleOne.is_kick == 0).all()
        return combos


@module_one_ns.route("/is_kick")
class CombosWithKick(Resource):

    @module_one_ns.marshal_list_with(module_one_dto)
    def get(self):
        """Get list of combinations that involve kick"""
        combos = ModuleOne.query.filter(ModuleOne.is_kick == 1).all()
        return combos


@module_one_ns.route("/is_jump")
class CombosWithJump(Resource):

    @module_one_ns.marshal_list_with(module_one_dto)
    def get(self):
        """Get list of combinations that involve jump"""
        combos = ModuleOne.query.filter(ModuleOne.is_jump == 1).all()
        return combos


@module_one_ns.route("/is_jump_kick")
class CombosWithJumpKick(Resource):

    @module_one_ns.marshal_list_with(module_one_dto)
    def get(self):
        """Get list of combinations that involve jump kick"""
        combos = ModuleOne.query.filter(ModuleOne.is_kick == 1, ModuleOne.is_jump == 1).all()
        return combos
