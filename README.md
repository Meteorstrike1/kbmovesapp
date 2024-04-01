# Kickboxing Moves App
## About
This app is currently in progress. It is a reference/practice tool based on my Kickboxing club's main grade syllabus up
to blackbelt.

## Motivation
I wanted to make an app so that I could easily search for moves from the combination I was doing, find which belt or 
lesson they are from, and look up technical details (twist or no twist, kick height etc). I also wanted to practice 
moves (or combinations) in whatever order I wanted, without my 10+ paper lists of moves in front me. Be able to practice
with a stopwatch or timer, save your lists or progress to return to, and a count of different speeds to try to keep up 
with (if I could make an erratic blackbelt mode that counts at lightning speed whilst randomly telling you to turn and 
change stance 4 times in a row then that would be a bonus). The ability to build a list of moves to go through 
(for example):
- from a certain belt
- moves that appear in the blackbelt modules
- moves that don't appear in the blackbelt modules that haven't practised for years
- even filter by if they involve jumps or kicks (which unfortunately has been motivated by my injury but still nice to 
choose leggy moves or just arms depending on how you feel)

## Tech stack
Built with Python, Kivy, and [KivyMD](https://github.com/kivymd/KivyMD) with a SQLite database.

## Features
- All 164 moves from main grade red white to blackbelt
- List of hand and leg defences
- Colour combinations
- Blackbelt module combinations
- Sparring combinations
- Freeform 1
- Possibly also self defence (but a little worried how to translate this to text)
- Ability to see related moves, combinations the moves are featured in, etc
- Filter by belt, lesson plan, defence, kick, jump, in module etc
- Practice mode to build list of moves to practice or use standard list (module 1, module 2, belt colour etc)