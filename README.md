Hangman Game
Author: Aziz Ahmad
Internship: CodeAlpha
Task 1: Hangman Game

Overview
This project is a Python-based Hangman game developed as part of an internship with CodeAlpha. The game challenges players to guess a hidden word by suggesting letters within a limited number of guesses. The game includes multiple difficulty levels, hint options, and tracks the player’s score and time spent playing.

How It Works
Game Initialization

When the game starts, the player is prompted to enter their name and age. Then, they must choose a difficulty level:
Easy: The player selects a category and can receive up to 2 hints. The hints can reveal letters or the category of the word.
Medium: The category is selected randomly. The player can receive up to 2 hints, including a letter or the category.
Hard: The category is selected randomly. No hints are available.
Choosing a Word

The game selects a word from a predefined list based on the chosen category and difficulty level. The player then tries to guess the word one letter at a time.
Gameplay

Guesses: The player has 6 incorrect guesses before the game ends.
Hints: Depending on the level, the player can use hints to reveal letters or the category of the word. Using a hint deducts 5 points from the score.
Score: Each correct guess increases the score by 10 points, while each incorrect guess decreases it by 5 points.
Ending the Game

If the player guesses the word before exhausting all attempts, they win the round, and the game prompts them to play again.
If the player fails to guess the word after 6 incorrect guesses, the game reveals the word and ends the round.
After each round, the player can choose to play again or exit the game. Upon exit, the player's total score and playtime are saved to a history file.
Logging and History

The game logs the player’s name, age, total score, and time spent playing in a file named history.txt. This log helps track progress over multiple sessions. 
