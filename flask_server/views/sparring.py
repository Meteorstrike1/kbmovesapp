from models import SparringCombination, Moves
from .moves import moves_dto
from flask_restx import Resource, fields, Namespace
from flask import abort


sparring_ns = Namespace("sparring", description="Namespace for sparring combinations")

sparring_dto = sparring_ns.model("SparringCombination", {
    "id": fields.Integer,
    "code": fields.String,
    "belt_colour": fields.String,
    "attack": fields.String,
    "defence": fields.String,
    "attack_id": fields.String,
    "defence_id": fields.String,
    "notes": fields.String
})


@sparring_ns.route("/all")
class SparCombosAll(Resource):
    @sparring_ns.marshal_list_with(sparring_dto)
    def get(self):
        """Get all sparring combinations"""
        combos = SparringCombination.query.all()
        return combos


@sparring_ns.route("/id/<int:id>")
class SparCombosById(Resource):
    @sparring_ns.marshal_with(sparring_dto)
    def get(self, id):
        """Get combination by id"""
        combos = SparringCombination.query.get_or_404(id)
        return combos

@sparring_ns.route("/belt/<string:colour>")
class SparCombosByColour(Resource):

    @sparring_ns.marshal_list_with(sparring_dto)
    def get(self, colour):
        """Get combination by belt colour"""
        combos = SparringCombination.query.filter(SparringCombination.belt_colour == colour).all()
        if len(combos) == 0:
            return abort(404, "No combinations found")
        return combos


@sparring_ns.route("/attack_move/<int:id>")
class SparComboAttackById(Resource):

    @sparring_ns.marshal_with(moves_dto)
    def get(self, id):
        """Get attack that appears in the sparring combination"""
        combo_moves = SparringCombination.query.filter(SparringCombination.id == id).first_or_404().attack_id
        if combo_moves is None:
            return abort(404, "No combination moves")
        attack_move = Moves.query.filter(Moves.code == combo_moves).first_or_404()
        return attack_move

@sparring_ns.route("/defence_moves/<int:id>")
class SparComboDefenceById(Resource):

    @sparring_ns.marshal_list_with(moves_dto)
    def get(self, id):
        """Get list of defences that appear in the sparring combination"""
        combo_moves = SparringCombination.query.filter(SparringCombination.id == id).first_or_404().defence_id
        if combo_moves is None:
            return abort(404, "No combination moves")

        no_whitespace = combo_moves.replace(" ", "")
        list_moves = no_whitespace.split(",")
        defence_moves = Moves.query.filter(Moves.code.in_(list_moves)).order_by(Moves.id).all()
        if len(defence_moves) == 0:
            return abort(404, "Combination defences could not be found")

        return defence_moves
