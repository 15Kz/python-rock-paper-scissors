# Rock Paper Scissors (Python)

A simple console-based Rock Paper Scissors game where you play against a computer opponent that picks its move at random.

## About This Project

I'm a first-year BS Information Technology student relearning Python while also learning C++. This project is my practice for the `random` library, along with core fundamentals like loops, user input, lists, and conditional logic.

## Features

- Computer picks Rock, Paper, or Scissor randomly using `random.choice()`
- Runs continuously, so you can play round after round
- Handles invalid input (anything other than the exact choice names counts as invalid)
- Reports a win, loss, or tie each round

## Concepts Practiced

- The `random` module
- Lists
- `while` loops
- `input()` and `print()`
- `if / elif / else` and logical operators (`and`, `or`)

## How to Run

1. Install Python 3
2. Download or clone this repository
3. Run the file with Python from your terminal

## How to Play

1. Run the program and the menu of choices appears
2. Type your choice exactly as written: `Rock`, `Paper`, or `Scissor` (capital first letter, no extra spaces)
3. The computer's random pick is compared with yours
4. The result (win, lose, or tie) is displayed, then a new round starts

## Game Rules

- Rock beats Scissor
- Paper beats Rock
- Scissor beats Paper
- Same choice on both sides is a tie

## Future Improvements

- Let the player type choices more flexibly (for example, lowercase)
- Show what the computer picked each round
- Add a score counter
- Add a way to quit the game
- Add a best-of-N mode
