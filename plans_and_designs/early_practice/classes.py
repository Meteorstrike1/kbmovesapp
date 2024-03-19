from dataclasses import dataclass, KW_ONLY, field, asdict
from abc import ABC, abstractmethod
from pprint import pprint as pp
import json

# To do
# Make a list for all the instances


# name, id, belt colour, lesson plan, related move (default []), in module combo (default []),
# # hand defence (default false), leg defence (default false), kick (default false),
# # jump (default false), notes (default ""), comments (default "")

@dataclass
class Move:
    move_total = 0
    move_name: str
    id_code: str
    belt_colour: str
    lesson_plan: int
    related_moves: list = field(default_factory=list)
    in_module_combo: list = field(default_factory=list)  # or related in module
    is_hand_defence: bool = False
    is_leg_defence: bool = False
    is_kick: bool = False
    is_jump: bool = False
    notes: str = ""
    comments: str = ""

    def add_comment(self):
        self.comments = input("Add a comment: ")

    @classmethod
    def number_of_moves(cls):
        return cls.move_total
