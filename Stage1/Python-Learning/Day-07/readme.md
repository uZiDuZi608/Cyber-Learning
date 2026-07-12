# 🐍 Day 7 – Hangman Game (Python)

## 📖 Overview

This repository documents my progress on **Day 7** of learning Python, where I built a fully functional **Hangman** game. The project focused on combining previously learned Python concepts such as loops, lists, strings, functions, conditionals, and modules into a complete command-line application.

The game randomly selects a word, tracks player guesses, updates the displayed word, manages lives, and provides visual feedback using ASCII art.

---

## 🎯 Learning Objectives

* Build a complete command-line game using Python.
* Work with lists to store and update game state.
* Manipulate strings using indexing and `.join()`.
* Use loops for continuous gameplay.
* Import and organize code using multiple Python modules.
* Apply logical thinking to solve game mechanics.

---

## 🧠 Core Concepts

### 🔹 Lists & Indexing

* Created a display list to represent hidden letters.
* Updated specific positions using list indexes.
* Preserved previously guessed correct letters throughout the game.

```python
display[i] = letter
```

### 🔹 Loops

* Used `while` loops to keep the game running until the player won or lost.
* Used `for` loops with `enumerate()` to compare each letter of the secret word.

```python
while word != chosen_word:
    ...
```

### 🔹 Conditional Statements

* Checked whether guesses were correct or incorrect.
* Managed player lives.
* Prevented duplicate guesses from affecting gameplay.

### 🔹 String Manipulation

* Converted the display list into a readable word using:

```python
word = "".join(display)
```

### 🔹 Python Modules

Imported external files to improve code organization:

* `hangman_words.py`
* `hangman_art.py`

Used the `random` module to select a random word each game.

---

## 🎮 Hangman Project Features

### ✅ Random Word Selection

A random word is selected from a predefined word list at the start of every game.

### ✅ Hidden Word Display

The game displays underscores representing each letter of the secret word.

### ✅ Letter Guessing

Players guess one letter at a time.

Correct guesses reveal all matching positions in the word.

### ✅ Lives System

Players begin with **6 lives**.

Each incorrect guess removes one life and updates the Hangman ASCII art.

### ✅ Duplicate Guess Detection

Previously guessed letters are detected and the player is notified without losing a life.

Example:

```text
You've already guessed a
```

### ✅ Game Over & Win Conditions

* Displays the completed word when the player wins.
* Reveals the correct word when the player loses.

---

## 📊 Skills Developed

✅ List Manipulation

✅ String Handling

✅ Indexing & Enumeration

✅ Algorithmic Thinking

✅ Problem Solving

✅ Control Flow

✅ Debugging

✅ Modular Programming

---

## 📁 Project Structure

```text
.
├── main.py
├── hangman_art.py
├── hangman_words.py
└── README.md
```

---

## ✔ Features Implemented

✔ Random word generation

✔ Hidden word display

✔ Continuous guessing loop

✔ Correct letter tracking

✔ Incorrect guess handling

✔ Lives management

✔ ASCII Hangman stages

✔ Duplicate guess detection

✔ Win condition

✔ Lose condition

✔ Modular code using imports

---

## 🚀 Key Takeaways

* Lists are ideal for storing and updating changing game data.
* `enumerate()` simplifies working with indexes and values simultaneously.
* Separating code into modules improves readability and maintainability.
* Breaking complex problems into smaller logical steps makes debugging easier.
* Building a complete project reinforces multiple Python concepts at once.

---

## 📌 Future Improvements

* Add difficulty levels (Easy, Medium, Hard).
* Allow players to play multiple rounds.
* Load words from external text files.
* Add categories for words.
* Display previously guessed letters in sorted order.
* Validate invalid inputs such as numbers or multiple characters.
* Refactor the code into reusable functions.
* Add score tracking and statistics.

---

## 🏁 Conclusion

Day 7 marked the transition from learning individual Python concepts to combining them into a complete application. Developing the Hangman game strengthened my understanding of loops, lists, indexing, string manipulation, modular programming, and game logic while improving my debugging and problem-solving skills.
