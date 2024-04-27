from models import ColourCombination, Moves
from .moves import moves_dto
from flask_restx import Resource, fields, Namespace
from flask import abort


colour_ns = Namespace("colour", description="Namespace for colour combinations")

colour_dto = colour_ns.model("ColourCombination", {
    "id": fields.Integer,
    "name": fields.String,
    "code": fields.String,
    "belt_colour": fields.String,
    "lesson_plan": fields.String,
    "moves": fields.String,
    "is_grading": fields.Boolean,
    "notes": fields.String
})


@colour_ns.route("/all")
class ColourCombosAll(Resource):
    @colour_ns.marshal_list_with(colour_dto)
    def get(self):
        """Get all colour combinations"""
        combos = ColourCombination.query.all()
        return combos


@colour_ns.route("/id/<int:id>")
class ColourCombosById(Resource):
    @colour_ns.marshal_with(colour_dto)
    def get(self, id):
        """Get combination by id"""
        combos = ColourCombination.query.get_or_404(id)
        return combos


@colour_ns.route("/belt/<string:colour>")
class ColourCombosByBelt(Resource):

    @colour_ns.marshal_list_with(colour_dto)
    def get(self, colour):
        """Get combination by belt colour"""
        combos = ColourCombination.query.filter(ColourCombination.belt_colour == colour).all()
        if len(combos) == 0:
            return abort(404, "No combinations found")
        return combos


@colour_ns.route("/combo_moves/<int:id>")
class ColourComboMovesById(Resource):

    @colour_ns.marshal_list_with(moves_dto)
    def get(self, id):
        """Get list of moves that appear in the combination"""
        combo_moves = ColourCombination.query.filter(ColourCombination.id == id).first_or_404().moves

        if combo_moves is None:
            return abort(404, "No combination moves")

        no_whitespace = combo_moves.replace(" ", "")
        list_moves = no_whitespace.split(",")
        moves = Moves.query.filter(Moves.code.in_(list_moves)).order_by(Moves.id).all()
        if len(moves) == 0:
            return abort(404, "Combination moves could not be found")

        return moves


@colour_ns.route("/is_grading")
class ColourCombosGrading(Resource):

    @colour_ns.marshal_list_with(colour_dto)
    def get(self):
        """Get list of grading combinations"""
        combos = ColourCombination.query.filter(ColourCombination.is_grading == 1).all()
        return combos


@colour_ns.route("/not_grading")
class ColourCombosGrading(Resource):

    @colour_ns.marshal_list_with(colour_dto)
    def get(self):
        """Get list of non grading combinations"""
        combos = ColourCombination.query.filter(ColourCombination.is_grading == 0).all()
        return combos
