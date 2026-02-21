# Hangman Game - Python Console Game

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A classic text-based Hangman game implemented in Python as part of my CodeAlpha Python Development Internship. This simple yet entertaining game challenges players to guess a secret word one letter at a time while managing their limited wrong attempts.

## 📋 Overview

This Hangman game is a console-based implementation that allows users to play the classic word-guessing game. The program randomly selects a word from a predefined list and challenges the player to guess it within 6 incorrect attempts.

## ✨ Features

- **Random Word Selection**: Game randomly picks from 5 predefined words
- **Limited Attempts**: Players get 6 wrong guesses before game over
- **Input Validation**: Ensures only single alphabetic characters are accepted
- **Progress Tracking**: Visual display of guessed letters and word progress
- **Duplicate Prevention**: Alerts players if they repeat letters
- **Game Statistics**: Shows number of wrong guesses and correctly guessed letters at the end

## 🛠️ Technologies Used

- **Python 3.x**
  - `random` module for word selection
  - Basic Python concepts: loops, conditionals, lists, string manipulation

## 🎯 How to Play

1. Run the Python script
2. The game will display underscores representing each letter in the secret word
3. Guess one letter at a time
4. Correct guesses reveal the letter's position(s)
5. Wrong guesses count toward your 6-attempt limit
6. Win by guessing all letters before running out of attempts

## 📁 Project Structure
hangman-game/
│
├── hangman_game.py # Main game script
├── README.md # Project documentation


## 🚀 Installation & Usage

### Prerequisites
- Python 3.x installed on your system

### Steps to Run

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/CodeAlpha_HangmanGame.git
   cd CodeAlpha_HangmanGame
2. Run the game
   ```bash
   python hangman_game.py


### 🎮 Gameplay Example
<br>
Hey! Welcome to Hangman Game!<br>
Find the Secret Word.<br>
You only get 6 wrong guesses. Good luck!<br>
--------------------<br>
Word has 6 letters: _ _ _ _ _ _<br>

Guess a letter: e<br>
'e' is not in the word. Try again!<br>
Wrong guesses: 1/6<br>

Word: _ _ _ _ _ _<br>
Wrong letters: e<br>

### 📊 Code Structure
hangman_game(): Main game function containing all game logic

Word list: Predefined collection of 5 words

Game loop: Manages turns, guesses, and win/loss conditions

Input validation: Ensures valid user input

### 🔍 Key Learning Concepts
Working with Python's random module

String and list manipulation

While loops and conditional statements

User input validation

Game logic implementation

### 📝 Future Enhancements
Add difficulty levels (change word length and attempt limits)

Include a larger word database

Add ASCII art for the hangman figure

Implement a scoring system

Add option to play multiple rounds

### 🤝 Contributing
This project was completed as part of my internship tasks. While it's not open for direct contributions, feel free to fork and customize it for your own learning!

### 📬 Contact
Author: Md. Minhazul Mowla

Internship: CodeAlpha Python Development

Project Completion: 5 February 2026

LinkedIn Post: https://www.linkedin.com/posts/md-minhazul-mowla_codealpha-internship-remoteintern-activity-7422482525371080705-WP4u?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEMykdcBnyGS_JGi_AlJEpxA2oo8BqbrhJw

### 🙏 Acknowledgments
CodeAlpha for providing this internship opportunity

Python community for excellent documentation and resources

<div align="center"> Made with ❤️ for CodeAlpha Python Development Internship </div>
