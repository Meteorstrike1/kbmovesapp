import dataclasses
from classes import Move

rw2 = Move("snap punch", "RW1", "red/white", 1, notes="note", in_module_combo=[1])

rw3 = Move("front kick front leg", "RW3", "red/white", 1, related_moves=["RW4"], in_module_combo=["M1_1", "M1_23"],
         is_kick=True)
# print(rw2)
print(rw3)

rw2_dict = dataclasses.asdict(rw2)
print(rw2_dict)
# rw2.add_comment()
# print(rw2)

# name, id, belt colour, lesson plan, related move (default []), in module combo (default []),
# # hand defence (default false), leg defence (default false), kick (default false),
# # jump (default false), notes (default ""), comments (default "")

red_white = [
    Move("snap punch", "RW1", "red/white", 1, in_module_combo=["M1_1"]),
    Move("reverse punch", "RW2", "red/white", 1, in_module_combo=["M1_1", "M1_2"]),
    Move("front kick front leg", "RW3", "red/white", 1, related_moves=["RW4"], in_module_combo=["M1_1", "M1_23"],
         is_kick=True),
    Move("front kick back leg", "RW4", "red/white", 2, related_moves=["RW3"], in_module_combo=["M1_6", "M1_11"],
         is_kick=True),
    Move("downward inside deflection front arm", "RW5", "red/white", 2, related_moves=["YW12"],
         in_module_combo=["M1_2"], is_hand_defence=True),
    Move("backfist front arm", "RW6", "red/white", 3, related_moves=["RW7"], in_module_combo=["M1_2", "M1_23"]),
    Move("backfist back arm", "RW7", "red/white", 3, related_moves=["RW6"], in_module_combo=["M1_3"]),
    Move("roundhouse kick back leg", "RW8", "red/white", 3, related_moves=["RW9", "R6"],
         in_module_combo=["M1_3", "M1_6", "M1_13"], is_kick=True),
    Move("roundhouse kick back leg land forward", "RW9", "red/white", 3, related_moves=["RW8", "R6"],
         in_module_combo=["M1_6"], is_kick=True),
    Move("palm deflection front arm", "RW10", "red/white", 4, related_moves=["RW11"], in_module_combo=["M1_3"],
         is_hand_defence=True),
    Move("palm deflection back arm", "RW11", "red/white", 4, related_moves=["RW10"], in_module_combo=["M1_21"],
         is_hand_defence=True, notes="Back foot doesn't twist"),
    Move("turn", "RW12", "red/white", 4)
]

red = [
    Move("rising punch front arm", "R1", "red", 1, related_moves=["R2"], in_module_combo=["M1_4", "M1_22"]),
    Move("rising punch back arm", "R2", "red", 1, related_moves=["R1"], in_module_combo=["M1_4", "M1_22"]),
    Move("roundhouse punch front arm", "R3", "red", 1, related_moves=["R4"], in_module_combo=["M1_4"]),
    Move("roundhouse punch back arm", "R4", "red", 1, related_moves=["R3"], in_module_combo=["M1_4"]),
    Move("downward evasion", "R5", "red", 2, in_module_combo=["M1_25"]),
    Move("roundhouse kick front leg", "R6", "red", 2, related_moves=["RW8", "RW9"], in_module_combo=["M1_4", "M1_23"],
         is_kick=True),
    Move("sliding snap punch", "R7", "red", 3, in_module_combo=["M1_8"]),
    Move("side kick front leg", "R8", "red", 3, related_moves=["R9", "R10"], in_module_combo=["M1_6", "M1_13"],
         is_kick=True),
    Move("side kick back leg", "R9", "red", 3, related_moves=["R8", "R10"], in_module_combo=["M1_6", "M1_13"],
         is_kick=True),
    Move("side kick back leg land forward", "R10", "red", 3, related_moves=["R8", "R9"], in_module_combo=["M1_6"],
         is_kick=True),
    Move("downward outside deflection front arm", "R11", "red", 4, related_moves=["Y4"], in_module_combo=["M1_13"],
         is_hand_defence=True),
    Move("one step front kick", "R12", "red", 4, related_moves=["RW3"], in_module_combo=["M1_14"],
         is_kick=True),
]

yellow_white = [
    Move("roundhouse elbow strike front arm", "YW1", "yellow/white", 1, related_moves=["YW2"],
         in_module_combo=["M1_5", "M1_22"], notes="Front foot twists"),
    Move("roundhouse elbow strike back arm", "YW2", "yellow/white", 1, related_moves=["YW1"],
         in_module_combo=["M1_12"]),
    Move("spinning backfist", "YW3", "yellow/white", 1, related_moves=["O11"], in_module_combo=["M1_7"]),
    Move("hook kick front leg", "YW4", "yellow/white", 2, related_moves=["YW6"], is_kick=True),
    Move("outside forearm block front arm", "YW5", "yellow/white", 2, related_moves=["OW7"], is_hand_defence=True),
    Move("hook kick back leg", "YW6", "yellow/white", 2, related_moves=["YW4"], is_kick=True),
    Move("stepping snap punch", "YW7", "yellow/white", 3, related_moves=["GW7"], in_module_combo=["M1_8", "M1_22"]),
    Move("front knee kick", "YW8", "yellow/white", 3, in_module_combo=["M1_12", "M1_25"], is_kick=True),
    Move("wing block front arm", "YW9", "yellow/white", 4, related_moves=["YW10"], in_module_combo=["M1_5"],
         is_hand_defence=True, notes="Front foot twists"),
    Move("wing block back arm", "YW10", "yellow/white", 4, related_moves=["YW9"], in_module_combo=["M1_5"],
         is_hand_defence=True),
    Move("one step side kick", "YW11", "yellow/white", 4, related_moves=["R8"], in_module_combo=["M1_14"],
         is_kick=True),
    Move("downward inside deflection back arm", "YW12", "yellow/white", 4, related_moves=["RW5"],
         in_module_combo=["M1_2"], is_hand_defence=True)
]

yellow = [
    Move("jump backfist", "Y1", "yellow", 1, in_module_combo=["M1_10"], is_jump=True,
         notes="Height not distance, aim slightly lower, rock back"),
    Move("sliding reverse punch", "Y2", "yellow", 1, in_module_combo=["M1_8"]),
    Move("one step roundhouse kick", "Y3", "yellow", 2, related_moves=["R6"], in_module_combo=["M1_14"], is_kick=True),
    Move("downward outside deflection back arm", "Y4", "yellow", 2, related_moves=["R11"], in_module_combo=["M1_13"],
         is_hand_defence=True),
    Move("roundhouse knee kick", "Y5", "yellow", 3, is_kick=True),
    Move("heel front stamp kick", "Y6", "yellow", 3, in_module_combo=["M1_10"], is_kick=True,
         notes="Push rather than a kick, at least chest height, land foot softly"),
    Move("side step to the front", "Y7", "yellow", 4, related_moves=["Y8"], in_module_combo=["M1_11"]),
    Move("side step to the back", "Y8", "yellow", 4, related_moves=["Y7"], in_module_combo=["M1_24"]),
    Move("rising forearm block", "Y9", "yellow", 4, in_module_combo=["M1_12"], is_hand_defence=True,
         notes="No twist, front arm only")
]

orange_white = [
    Move("spinning elbow strike", "OW1", "orange/white", 1, in_module_combo=["M1_7"]),
    Move("downward backfist front arm", "OW2", "orange/white", 1, related_moves=["OW3"]),
    Move("downward backfist back arm", "OW3", "orange/white", 1, related_moves=["OW2"]),
    Move("back kick", "OW4", "orange/white", 2, in_module_combo=["M1_9"], is_kick=True),
    Move("jump back backfist", "OW5", "orange/white", 2, in_module_combo=["M1_19"], is_jump=True,
         notes="Height not distance, aim slightly lower, rock back"),
    Move("outside axe kick", "OW6", "orange/white", 3, related_moves=["O6"], in_module_combo=["M1_19"], is_kick=True,
         notes="Shoulder or head height, land foot softly"),
    Move("outside forearm block back arm", "OW7", "orange/white", 4, related_moves=["YW5"], is_hand_defence=True),
    Move("double kick (front kick, roundhouse kick)", "OW8", "orange/white", 4, in_module_combo=["M1_23"],
         is_kick=True),
    Move("double kick (side kick, hook kick)", "OW9", "orange/white", 4, is_kick=True),
    Move("double kick (roundhouse kick, side kick)", "OW10", "orange/white", 4, in_module_combo=["M1_13"],
         is_kick=True),
    Move("double kick (hook kick, roundhouse kick)", "OW11", "orange/white", 6, is_kick=True)
]

orange = [
    Move("palm heel strike front arm", "O1", "orange", 1, related_moves=["O2"], in_module_combo=["M1_15", "M1_21"]),
    Move("palm heel strike back arm", "O2", "orange", 1, related_moves=["O1"], in_module_combo=["M1_15", "M1_21"]),
    Move("hammerfist strike front arm", "O3", "orange", 1, related_moves=["O4"], in_module_combo=["M1_15", "M1_24"]),
    Move("hammerfist strike back arm", "O4", "orange", 1, related_moves=["O3"], in_module_combo=["M1_15", "M1_24"]),
    Move("inside forearm block front arm", "O5", "orange", 2, related_moves=["GW6"], in_module_combo=["M1_7"],
         is_hand_defence=True, notes="Front foot twists"),
    Move("inside axe kick", "O6", "orange", 2, related_moves=["OW6"], in_module_combo=["M1_18"], is_kick=True,
         notes="Shoulder or head height, land foot softly"),
    Move("ball of foot roundhouse kick front leg", "O7", "orange", 3, related_moves=["O8"], in_module_combo=["M1_15"],
         is_kick=True),
    Move("ball of foot roundhouse kick back leg", "O8", "orange", 3, related_moves=["O7"], in_module_combo=["M1_15"],
         is_kick=True),
    Move("sliding snap reverse punch", "O9", "orange", 3, related_moves=["R7", "Y2"], in_module_combo=["M1_11"]),
    Move("spinning hook kick", "O10", "orange", 4, related_moves=["BW12"], in_module_combo=["M1_5", "M1_20"],
         is_kick=True),
    Move("forward spinning backfist", "O11", "orange", 4, related_moves=["YW3"], in_module_combo=["M1_20"])
]

green_white = [
    Move("ridgehand strike front arm", "GW1", "green/white", 1, related_moves=["GW3"], in_module_combo=["M1_16"],
         notes="Aim to neck, front leg twists"),
    Move("jump front kick front leg", "GW2", "green/white", 1, related_moves=["BW6"], in_module_combo=["M1_19"],
         is_kick=True, is_jump=True),
    Move("ridgehand strike back arm", "GW3", "green/white", 1, related_moves=["GW1"], in_module_combo=["M1_21"],
         notes="Aim to neck"),
    Move("knuckle punch front arm", "GW4", "green/white", 2, related_moves=["GW5"], in_module_combo=["M1_24"],
         notes="Aim to neck, knuckle shape, like a snap punch"),
    Move("knuckle punch back arm", "GW5", "green/white", 2, related_moves=["GW4"], in_module_combo=["M1_16"],
         notes="Aim to neck, knuckle shape, like a reverse punch"),
    Move("inside forearm block back arm", "GW6", "green/white", 2, related_moves=["O5"], in_module_combo=["M1_18"],
         is_hand_defence=True),
    Move("stepping snap reverse punch", "GW7", "green/white", 3, related_moves=["YW7"],
         in_module_combo=["M1_8", "M1_22"]),
    Move("spinning back kick", "GW8", "green/white", 3, is_kick=True),
    Move("pressing block front arm", "GW9", "green/white", 4, related_moves=["GW11"], in_module_combo=["M1_16"],
         is_hand_defence=True),
    Move("footsweep", "GW10", "green/white", 4),
    Move("pressing block front arm", "GW11", "green/white", 4, related_moves=["GW9"], in_module_combo=["M1_16"],
         is_hand_defence=True)
]

green = [
    Move("palm heel strike to groin front arm", "G1", "green", 1, related_moves=["G3"],
         in_module_combo=["M1_17", "M1_25"], notes="Shoulder drops down"),
    Move("jump snap punch", "G2", "green", 1, in_module_combo=["M1_10"],
         notes="Height not distance, aim slightly lower, rock back"),
    Move("palm heel strike to groin back arm", "G3", "green", 1, related_moves=["G1"],
         in_module_combo=["M1_17", "M1_25"], notes="Shoulder drops down"),
    Move("straight leg roundhouse kick", "G4", "green", 2, related_moves=["P9"], is_kick=True,
         notes="Shin makes contact"),
    Move("downward hook deflection", "G5", "green", 2, in_module_combo=["M1_17"], is_hand_defence=True),
    Move("jump roundhouse kick", "G6", "green", 3, in_module_combo=["M1_17"], is_kick=True, is_jump=True),
    Move("jump hammerfist", "G7", "green", 3, is_jump=True, notes="Height not distance, aim slightly lower, rock back"),
    Move("inside knee block front leg", "G8", "green", 4, in_module_combo=["M1_9"], is_leg_defence=True),
    Move("take down", "G9", "green", 4)
]

blue_white = [
    Move("turning backfist", "BW1", "blue/white", 1, in_module_combo=["M2_1"]),
    Move("bolo reverse punch", "BW2", "blue/white", 1, in_module_combo=["M2_4"]),
    Move("hand jam", "BW3", "blue/white", 2, is_hand_defence=True),
    Move("leg jam heel front", "BW4", "blue/white", 2, related_moves=["BW5"], is_leg_defence=True),
    Move("leg jam heel side", "BW5", "blue/white", 2, related_moves=["BW4"], is_leg_defence=True),
    Move("jump front kick back leg", "BW6", "blue/white", 2, related_moves=["GW2"], in_module_combo=["M2_2"],
         is_kick=True, is_jump=True),
    Move("ridgehand strike to groin front arm", "BW7", "blue/white", 3, related_moves=["BW8"],
         in_module_combo=["M2_1"], notes="Shoulder drops down"),
    Move("ridgehand strike to groin back arm", "BW8", "blue/white", 3, related_moves=["BW7"], in_module_combo=["M2_1"],
         notes="Shoulder drops down"),
    Move("inside crescent kick front leg", "BW9", "blue/white", 3, related_moves=["BW10"], in_module_combo=["M2_4"],
         is_kick=True),
    Move("inside crescent kick back leg", "BW10", "blue/white", 3, related_moves=["BW9"], in_module_combo=["M2_4"],
         is_kick=True),
    Move("reverse footsweep", "BW11", "blue/white", 4),
    Move("forward spinning hook kick", "BW12", "blue/white", 4, related_moves=["O10"], in_module_combo=["M2_6"],
         is_kick=True)
]

blue = [
    Move("reverse snap punch", "B1", "blue", 1, in_module_combo=["M2_2"], notes="Back arm, snappy, to the ribs"),
    Move("whipping roundhouse kick", "B2", "blue", 1, in_module_combo=["M2_1"], is_kick=True),
    Move("sliding roundhouse punch", "B3", "blue", 2, in_module_combo=["M2_8"]),
    Move("inside knife hand block front arm", "B4", "blue", 2, related_moves=["B5"], is_hand_defence=True,
         notes="Front foot twists"),
    Move("inside knife hand block back arm", "B5", "blue", 2, related_moves=["B4"], is_hand_defence=True),
    Move("outside crescent kick front leg", "B6", "blue", 3, related_moves=["B7"], in_module_combo=["M2_11"],
         is_kick=True),
    Move("outside crescent kick back leg", "B7", "blue", 3, related_moves=["B6"], in_module_combo=["M2_11"],
         is_kick=True),
    Move("jump reverse punch", "B8", "blue", 3, is_jump=True,
         notes="Height not distance, aim slightly lower, rock back"),
    Move("outside knife hand block front arm", "B9", "blue", 4, related_moves=["B10"], in_module_combo=["M2_11"],
         is_hand_defence=True),
    Move("outside knife hand block back arm", "B10", "blue", 4, related_moves=["B9"], in_module_combo=["M2_11"],
         is_hand_defence=True),
    Move("spinning reverse footsweep", "B11", "blue", 4, in_module_combo=["M2_11"],
         notes="Low as can, past centre line, back leg bent, front leg straight")
]

purple_white = [
    Move("jump spinning backfist", "PW1", "purple/white", 1, in_module_combo=["M2_7"], is_jump=True,
         notes="Jump and spin at the same time"),
    Move("spinning back elbow strike", "PW2", "purple/white", 1),
    Move("outside knee block front leg", "PW3", "purple/white", 2, related_moves=["PW8"], in_module_combo=["M2_9"],
         is_leg_defence=True),
    Move("jump back kick", "PW4", "purple/white", 2, in_module_combo=["M2_6", "M2_17"], is_kick=True, is_jump=True),
    Move("bolo rising punch", "PW5", "purple/white", 3),
    Move("turning side kick", "PW6", "purple/white", 3, related_moves=["Br11"], in_module_combo=["M2_7"], is_kick=True),
    Move("hip throw", "PW7", "purple/white", 4),
    Move("outside knee block back leg", "PW8", "purple/white", 4, related_moves=["PW3"], in_module_combo=["M2_9"],
         is_leg_defence=True)
]

purple = [
    Move("inside knife hand strike front arm", "P1", "purple", 1, related_moves=["P3"], in_module_combo=["M2_2"],
         notes="Aim to neck"),
    Move("sliding elbow strike", "P2", "purple", 1, in_module_combo=["M2_15"]),
    Move("inside knife hand strike back arm", "P3", "purple", 1, related_moves=["P1"], in_module_combo=["M2_2"],
         notes="Aim to neck"),
    Move("slide back hand defences", "P4", "purple", 2, related_moves=["BrW5"], notes="21 of them"),
    Move("jump front knee kick (to midsection)", "P5", "purple", 2, related_moves=["BrW4"], in_module_combo=["M2_9"],
         is_kick=True, is_jump=True),
    Move("outside knife hand strike front arm", "P6", "purple", 3, related_moves=["P7"],
         notes="Aim to neck, like a backfist"),
    Move("outside knife hand strike back arm", "P7", "purple", 3, related_moves=["P6"],
         notes="Aim to neck, like a backfist"),
    Move("spinning outside crescent kick", "P8", "purple", 3, is_kick=True),
    Move("double straight leg roundhouse kick", "P9", "purple", 4, related_moves=["P7"], is_kick=True,
         notes="Shin makes contact"),
    Move("slide back leg defences", "P10", "purple", 4, related_moves=["BrW10"],
         notes="Just 4 of them (all front leg)")
]

brown_white = [
    Move("rising elbow strike front arm", "BrW1", "brown/white", 1, related_moves=["BrW2"], in_module_combo=["M2_3"]),
    Move("rising elbow strike back arm", "BrW2", "brown/white", 1, related_moves=["BrW1"], in_module_combo=["M2_3"]),
    Move("spinning knife hand strike", "BrW3", "brown/white", 1, related_moves=["Br5"], in_module_combo=["M2_10"]),
    Move("jump front knee kick (to head)", "BrW4", "brown/white", 2, related_moves=["P5"], in_module_combo=["M2_3"],
         is_kick=True, is_jump=True),
    Move("step back hand defences", "BrW5", "brown/white", 2, related_moves=["P4"], in_module_combo=["M2_5"],
         notes="21 of them"),
    Move("straight arm backfist front arm", "BrW6", "brown/white", 3, related_moves=["BrW7"],
         notes="Front leg twists, let it go"),
    Move("straight arm backfist back arm", "BrW7", "brown/white", 3, related_moves=["BrW6"], notes="Let it go"),
    Move("one step axe kick", "BrW8", "brown/white", 3, related_moves=["OW6", "O6"], in_module_combo=["M2_13"],
         is_kick=True, notes="Inside or outside, shoulder or head height, land foot softly"),
    Move("spinning roundhouse kick", "BrW9", "brown/white", 4, in_module_combo=["M2_13"], is_kick=True,
         notes="Step across, knee blocking, roundhouse kick back leg land forward"),
    Move("step back leg defences", "BrW10", "brown/white", 4, related_moves=["P10"], in_module_combo=["M2_16"],
         notes="Just 4 of them (all font leg)")
]

brown = [
    Move("whipping elbow strike front arm", "Br1", "brown", 1, related_moves=["Br2"], in_module_combo=["M2_3"]),
    Move("whipping elbow strike back arm", "Br2", "brown", 1, related_moves=["Br1"], in_module_combo=["M2_3"]),
    Move("jump scissor front kick front leg", "Br3", "brown", 1, related_moves=["Br4"],
         in_module_combo=["M2_5", "M2_14"], is_kick=True, is_jump=True),
    Move("jump scissor front kick back leg", "Br4", "brown", 1, related_moves=["Br3"],
         in_module_combo=["M2_18"], is_kick=True, is_jump=True),
    Move("forward spinning knife hand strike", "Br5", "brown", 2, related_moves=["BrW3"], in_module_combo=["M2_10"]),
    Move("rising elbow block", "Br6", "brown", 2, in_module_combo=["M2_12"], is_hand_defence=True,
         notes="Lean into it slightly"),
    Move("downward elbow block", "Br7", "brown", 2, is_hand_defence=True,
         notes="Lean forward slightly, not too low, aim in middle"),
    Move("arcing roundhouse punch front arm", "Br8", "brown", 3, related_moves=["Br9"]),
    Move("arcing roundhouse punch back arm", "Br9", "brown", 3, related_moves=["Br8"]),
    Move("straight arm spinning backfist", "Br10", "brown", 3, related_moves=["BrW7"], in_module_combo=["M2_12"]),
    Move("forward turning side kick", "Br11", "brown", 4, related_moves=["PW6"], in_module_combo=["M2_8"],
         is_kick=True)
]

junior_black = [
    Move("overarm reverse punch", "JB1", "junior black", 1, in_module_combo=["M2_5"]),
    Move("jump scissor axe kick front leg", "JB2", "junior black", 1, related_moves=["JB3"], in_module_combo=["M2_14"],
         is_kick=True, is_jump=True, notes="Inside or outside, shoulder or head height, land foot softly"),
    Move("jump scissor axe kick back leg", "JB3", "junior black", 1, related_moves=["JB2"],
         in_module_combo=["M2_16", "M2_18"], is_kick=True, is_jump=True,
         notes="Inside or outside, shoulder or head height, land foot softly"),
    Move("forward spinning inside crescent kick", "JB4", "junior black", 2, in_module_combo=["M2_6"], is_kick=True),
    Move("single knuckle punch front arm", "JB5", "junior black", 3, related_moves=["JB6"], in_module_combo=["M2_13"],
         notes="Make sure finger is locked in, aim to neck, like a snap punch"),
    Move("single knuckle punch back arm", "JB6", "junior black", 3, related_moves=["JB5"], in_module_combo=["M2_13"],
         notes="Make sure finger is locked in, aim to neck, like a reverse punch"),
    Move("rising front kick", "JB7", "junior black", 3, is_kick=True, notes="Front leg only, toes pointed"),
    Move("jump turning side kick", "JB8", "junior black", 4, in_module_combo=["M2_17"], is_kick=True, is_jump=True,
         notes="Jump and spin at the same time"),
    Move("reinforced forearm block", "JB9", "junior black", 8, is_hand_defence=True,
         notes="Back foot flat twist, palm on arm, tensed"),
    Move("double forearm block to the front", "JB10", "junior black", 8, related_moves=["JB11"], is_hand_defence=True),
    Move("double forearm block to the side", "JB11", "junior black", 8, related_moves=["JB10"], is_hand_defence=True)
]

black = [
    Move("flying side kick", "Bl1", "black", 3, related_moves=["Bl2"], in_module_combo=["M2_10"], is_kick=True,
         is_jump=True, notes="Tiny step with front leg, kick with back leg"),
    Move("one step flying side kick", "Bl2", "black", 3, related_moves=["Bl1"], in_module_combo=["M2_15"], is_kick=True,
         is_jump=True, notes="One step then kick with what was front leg"),
    Move("downward elbow strike front arm", "Bl3", "black", 3, related_moves=["Bl4"], in_module_combo=["M2_9"]),
    Move("downward elbow strike front arm", "Bl4", "black", 3, related_moves=["Bl3"], in_module_combo=["M2_9"])
]

print(rw2.move_name)
print(red_white[0].move_name)

for move in red_white:
    print(dataclasses.asdict(move))

for i in range(len(red_white)):
    print(red_white[i].move_name.capitalize())

# Carry on making the rest of the lists later

print(red[0].move_name)

for move in red:
    print(dataclasses.asdict(move))

for i in range(len(red)):
    print(red[i].move_name.capitalize())

print(Move.number_of_moves())

total_moves = [red_white + red + yellow_white]
print(total_moves)
print(type(total_moves))

print(Move.move_total)
print(type(red))
print(len(red))

# for i in total_moves:
#     total = 0
#     total += len(i)
#     print(total)


def create_move_list(*args):
    total = 0
    for i in args:
        total += len(i)
    created_list = [x for x in args]

    return created_list, total


created_list, total = create_move_list(red_white, red, yellow_white)
print(created_list)
print(len(created_list))
print(total)

