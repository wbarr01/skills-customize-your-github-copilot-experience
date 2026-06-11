
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game in Python to practice strings, loops, conditionals, lists, and user input.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description
Create a list of words and initialize the game state before the player starts guessing.

#### Requirements
Completed program should:

- Define a predefined list of words to choose from
- Randomly select one word for the current game
- Initialize the hidden word display using underscores
- Set a limited number of incorrect attempts

### 🛠️ Letter Guessing and Progress Display

#### Description
Accept player guesses, update the hidden word progress, and show incorrect guesses remaining.

#### Requirements
Completed program should:

- Prompt the player to guess a single letter
- Reveal correctly guessed letters in their positions
- Show the current word progress using underscores for unknown letters
- Track letters already guessed and handle repeated guesses gracefully

### 🛠️ Win/Lose Logic

#### Description
End the game with a win or lose message based on the player’s performance.

#### Requirements
Completed program should:

- Declare the player a winner when the full word is guessed
- End the game with a loss when attempts run out
- Display a clear win or lose message and reveal the correct word if the player loses
- Keep the game loop running until a final result is reached
