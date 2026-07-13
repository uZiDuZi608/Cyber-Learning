# 🐍 Day 9 – Dictionaries, Nesting & Secret Auction (Python)

## 📖 Overview

This repository documents my progress on **Day 9** of learning Python, where I explored **dictionaries**, **nesting**, and built a **Secret Auction** program.

The project focused on storing data using dictionaries, collecting multiple users' bids, iterating through stored data, and determining the highest bidder. This lesson strengthened my understanding of key-value data structures and how they can be used to organize and process information efficiently.

---

## 🎯 Learning Objectives

- Understand Python dictionaries.
- Learn how to add, update, and retrieve dictionary values.
- Iterate through dictionaries using `for` loops.
- Understand dictionary nesting.
- Store multiple users' bids in a dictionary.
- Find the highest bid by looping through stored data.
- Build a complete Secret Auction program.

---

## 🧠 Core Concepts

### 🔹 Dictionaries

Learned how to store data using **key-value pairs**.

```python
student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95
}
```

Each key is unique and maps to a corresponding value.

---

### 🔹 Accessing Dictionary Values

Retrieved values using their keys.

```python
score = student_scores["Harry"]
```

Output:

```
88
```

---

### 🔹 Adding & Updating Items

Added new entries or updated existing ones.

```python
student_scores["Draco"] = 75
```

Updated values simply by assigning a new value to an existing key.

---

### 🔹 Creating an Empty Dictionary

Created dictionaries to store data during program execution.

```python
bidding_record = {}
```

---

### 🔹 Looping Through Dictionaries

Iterated through dictionary keys using a `for` loop.

```python
for name in bidding_record:
    print(name)
```

Accessed each corresponding value using:

```python
bidding_record[name]
```

---

### 🔹 Conditional Statements

Used `if` statements to compare bids and determine the highest bidder.

```python
if bidding_record[name] > highest_bid:
    highest_bid = bidding_record[name]
    winner = name
```

---

### 🔹 While Loops

Used a `while` loop to continue accepting bids until there were no more bidders.

```python
while more != "no":
```

---

### 🔹 User Input

Collected bidder names and bid amounts using the `input()` function.

```python
name = input("What is your name? ")
price = int(input("How much do you want to bid? "))
```

---

## 🔨 Secret Auction Project Features

### ✅ Multiple Bidders

Allows multiple participants to enter their names and bids.

Example:

```
Name: Alice
Bid: 250

Name: Bob
Bid: 300

Name: Charlie
Bid: 275
```

---

### ✅ Store Bids in a Dictionary

Every bid is stored using the bidder's name as the key.

Example:

```python
{
    "Alice": 250,
    "Bob": 300,
    "Charlie": 275
}
```

---

### ✅ Find the Highest Bid

Loops through the dictionary after all bids have been collected and determines the winner.

Example Output:

```
The winner is Bob with a bid of $300.
```

---

### ✅ Hidden Auction

Clears the screen between bidders (using blank lines in this version) so each person's bid remains private.

---

### ✅ ASCII Logo

Imports an external `art.py` module to display the Secret Auction logo at the start of the program.

---

## 📊 Skills Developed

✅ Dictionaries

✅ Dictionary Traversal

✅ Dictionary Updates

✅ Key-Value Data Structures

✅ Loops

✅ While Loops

✅ Conditional Logic

✅ User Input Handling

✅ Data Storage

✅ Problem Solving

✅ Debugging

---

## 📁 Project Structure

```text
.
├── main.py
├── art.py
└── README.md
```

---

## ✔ Features Implemented

✔ Dictionary creation

✔ Adding key-value pairs

✔ User input collection

✔ Multiple bidder support

✔ Highest bid calculation

✔ Winner announcement

✔ Dictionary iteration

✔ ASCII logo import

✔ Hidden bidding interface

✔ Command-line application

---

## 🚀 Key Takeaways

- Dictionaries provide an efficient way to store related data using key-value pairs.
- Iterating through a dictionary makes it easy to process stored information.
- Separating data collection from data processing improves program organization.
- Loops allow programs to repeatedly collect user input.
- Conditional statements help compare values and determine results.
- Combining dictionaries with loops enables powerful data-processing applications.

---

## 📌 Future Improvements

- Validate invalid bid inputs.
- Prevent duplicate bidder names.
- Clear the terminal using operating system commands instead of blank lines.
- Allow multiple auction rounds.
- Save auction results to a text file.
- Display all bids after the auction ends.
- Add error handling using `try` and `except`.

---

## 🏁 Conclusion

Day 9 introduced dictionaries as a powerful way to organize and manage data using key-value pairs. Building the Secret Auction project reinforced how dictionaries, loops, conditionals, and user input work together to solve real-world problems.

This project strengthened my understanding of data storage, dictionary traversal, and algorithmic thinking while demonstrating how to process collections of information to determine meaningful results, such as identifying the highest bidder in an auction.