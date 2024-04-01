from extensions import db


class Moves(db.Model):
    """
    Class model for moves table.

    Attributes
    ----------
    id : int
        PK autoincrement, so can keep moves in learning order and can split syllabus for module 1 vs module 2
    name: str
        name of move
    code: str
        a more human friendly reference id for the moves, with belt shorthand and number
    belt_colour: str
        colour of belt
    lesson_plan: int
        lesson plan that the move first appears in, so can look up that video
    related_moves: str
        list of moves that are related to the move such as front/back, inside/outside
    module_combo: str
        id code of module combination that the move either appears in, or its relation appears in
    is_defence: str
        null if not a defence, hand if hand defence, leg if leg defence
    is_kick: bool
        if it is a kick
    is_jump: bool
        if it is a jump
    notes: str
        notes for move if required/helpful
    """

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


class ColourCombination(db.Model):
    """
    Class model for colour combinations table.

    Attributes
    ----------
    id : int
        PK autoincrement, so can keep colour combinations in learning order but not so important
    name: str
        name of combination
    code: str
        a more human friendly reference id for the combination, with belt shorthand and number
    belt_colour: str
        colour of belt
    lesson_plan: int
        lesson plans that the combination appears in, not so important could get rid of
    moves: str
        list of moves that appear in the combination
    is_grading: bool
        if it is a grading combination
    notes: str
        notes for combination if required/helpful
    """

    __tablename__ = "colour_combos"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    belt_colour = db.Column(db.String(15), nullable=False)
    lesson_plan = db.Column(db.String(50), nullable=False)
    moves = db.Column(db.String(50))
    is_grading = db.Column(db.Boolean, server_default="0")
    notes = db.Column(db.String(200))


class ModuleOne(db.Model):
    """
    Class model for module 1 combinations table.

    Attributes
    ----------
    id : int
        PK autoincrement, will be same as module number, could possibly use instead of code, keep both for now
    name: str
        name of combination
    code: str
        actually a less human friendly reference id for the combination since modules use just number
    moves: str
        list of moves that appear in the combination
    is_kick: bool
        if it involves a kick
    is_jump: bool
        if it involves a jump
    notes: str
        notes for combination if required/helpful
    """

    __tablename__ = "module_one"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    moves = db.Column(db.String(50))
    is_kick = db.Column(db.Boolean, server_default="0")
    is_jump = db.Column(db.Boolean, server_default="0")
    notes = db.Column(db.String(200))


class ModuleTwo(db.Model):
    """
    Class model for module 2 combinations table (identical to module one table I know but want to keep separate).

    Attributes
    ----------
    id : int
        PK autoincrement, will be same as module number, could possibly use instead of code, keep both for now
    name: str
        name of combination
    code: str
        actually a less human friendly reference id for the combination since modules use just number
    moves: str
        list of moves that appear in the combination
    is_kick: bool
        if it involves a kick
    is_jump: bool
        if it involves a jump
    notes: str
        notes for combination if required/helpful
    """

    __tablename__ = "module_two"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    moves = db.Column(db.String(50))
    is_kick = db.Column(db.Boolean, server_default="0")
    is_jump = db.Column(db.Boolean, server_default="0")
    notes = db.Column(db.String(200))


class SparringCombination(db.Model):
    """
    Class model for sparring combinations table.

    Attributes
    ----------
    id : int
        PK autoincrement, so can keep colour combinations in learning order but not so important
    code: str
        a more human friendly reference id for the combination, with belt shorthand and number
    belt_colour: str
        colour of belt
    attack: str
        name of move for the attack
    defence: str
        names of moves for the defence
    moves: str
        list of moves that appear in the attack/defence
    notes: str
        notes for combination if required/helpful
    """

    __tablename__ = "sparring_combos"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    belt_colour = db.Column(db.String(15), nullable=False)
    attack = db.Column(db.String(100), nullable=False)
    defence = db.Column(db.String(200), unique=True, nullable=False)
    moves = db.Column(db.String(50))
    notes = db.Column(db.String(200))
