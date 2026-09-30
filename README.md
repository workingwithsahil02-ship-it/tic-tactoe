# Tic-Tac-Toe

A simple tic-tac-toe game that runs in the terminal, made with Python. You can play against a friend or against the computer.

I made this to practice loops, functions and lists. It's not super fancy but it works!

## How to run it

You need Python 3 installed. No extra libraries needed (it only uses `random` which comes with python).

Open a terminal in the project folder and type:

```
python main.py
```

(if that doesnt work try `python3 main.py`)

## How to play

1. Pick a mode
   - `1` = play against a friend
   - `2` = play against the computer
2. Type in your name (or just press enter to use the default name)
3. The board shows numbers 1-9. Type the number of the spot you want to take

```
1 | 2 | 3
---+---+---
4 | 5 | 6
---+---+---
7 | 8 | 9
```

Player 1 is always **X** and goes first. Player 2 (or the computer) is **O**.

First one to get 3 in a row (across, down, or diagonal) wins. If the board fills up with no winner it's a tie.

## Features

- 2 player mode
- Play vs computer
- Checks if your input is valid (so it wont crash if you type letters or a number that's already taken)
- Custom player names
- Detects wins and ties

## Things I know aren't perfect

- The computer just picks a random empty spot, so its not really smart. You can beat it pretty easily lol
- No "play again" option, you have to run the program again
- Only works in the terminal, no graphics

## Ideas for later

- [ ] Make the computer smarter (maybe use minimax?)
- [ ] Add a play again button
- [ ] Keep track of score
- [ ] Maybe make a GUI version with tkinter

## Files

- `main.py` - the whole game is in here

Thanks for checking out my project!
