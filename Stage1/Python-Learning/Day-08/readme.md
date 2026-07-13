# 🐍 Day 8 – Functions & Caesar Cipher (Python)

## 📖 Overview

This repository documents my progress on **Day 8** of learning Python, where I explored **functions**, **function parameters**, **keyword arguments**, and built a complete **Caesar Cipher** encryption and decryption program.

The project focused on writing reusable functions, passing data through parameters, organizing program logic, handling user input, and creating a program that can repeatedly encrypt or decrypt messages while preserving spaces, numbers, and punctuation.

---

## 🎯 Learning Objectives

* Understand how to define and call functions.
* Learn the difference between positional and keyword arguments.
* Pass data into functions using parameters.
* Build reusable and modular code.
* Create a Caesar Cipher encryption and decryption program.
* Handle special characters and user input safely.
* Use loops to restart the program until the user chooses to quit.

---

## 🧠 Core Concepts

### 🔹 Defining Functions

Learned how to create reusable blocks of code using the `def` keyword.

```python
def greet():
    print("Hello World")
```

Functions improve code organization and reduce repetition.

---

### 🔹 Function Parameters & Arguments

Learned how to pass information into functions using parameters.

```python
def greet_with_name(name):
    print(f"Hello {name}")
```

Example:

```python
greet_with_name("John")
```

---

### 🔹 Multiple Parameters

Created functions that accept multiple pieces of information.

```python
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
```

---

### 🔹 Keyword Arguments

Learned that arguments can be passed by explicitly naming each parameter.

```python
greet_with(
    name="John",
    location="New York"
)
```

Keyword arguments improve readability and allow arguments to be passed in any order.

---

### 🔹 Loops

Used:

* `for` loops to process each character in a message.
* `while` loops to restart the cipher program until the user exits.

---

### 🔹 Conditional Statements

Used `if`, `elif`, and `else` to determine whether to:

* Encrypt
* Decrypt
* Preserve spaces and punctuation
* Continue or exit the program

---

### 🔹 String Manipulation

Built encrypted and decrypted messages one character at a time.

```python
encrypted_text += converted_letter
```

---

### 🔹 Modulo Operator (`%`)

Learned how modulo keeps alphabet indexes within range.

Example:

```python
34 % 26 = 8
```

This allows the cipher to wrap around the alphabet correctly.

Example:

```
z → a
z + 9 → i
```

---

## 🔐 Caesar Cipher Project Features

### ✅ Encryption

Shifts every alphabetical character forward by a user-selected amount.

Example:

```
hello
```

Shift:

```
5
```

Output:

```
mjqqt
```

---

### ✅ Decryption

Reverses the encryption by shifting letters backwards.

Example:

```
mjqqt
```

Shift:

```
5
```

Output:

```
hello
```

---

### ✅ Wrap Around Alphabet

Correctly handles letters near the end of the alphabet.

Examples:

```
z + 1 → a

z + 9 → i
```

using:

```python
new_index = (old_index + shift) % 26
```

---

### ✅ Preserve Spaces & Symbols

Numbers, spaces, and punctuation remain unchanged.

Example:

```
hello world! 123
```

becomes

```
mjqqt btwqi! 123
```

---

### ✅ Continuous Program

Allows the user to encrypt or decrypt multiple messages without restarting Python.

```
Type 'yes' if you want to go again.
Otherwise type 'no'.
```

---

### ✅ ASCII Logo

Imported an external `art.py` module to display the Caesar Cipher logo when the program starts.

---

## 📊 Skills Developed

✅ Function Creation

✅ Parameters & Arguments

✅ Keyword Arguments

✅ Function Calls

✅ String Manipulation

✅ Loops

✅ Conditional Logic

✅ Modular Programming

✅ User Input Handling

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

✔ Function definitions

✔ Function parameters

✔ Keyword arguments

✔ Caesar Cipher encryption

✔ Caesar Cipher decryption

✔ Alphabet wrap-around using modulo

✔ Space and punctuation preservation

✔ ASCII logo import

✔ Program restart functionality

✔ User-friendly command-line interface

---

## 🚀 Key Takeaways

* Functions allow code to be reused instead of repeated.
* Parameters make functions flexible by accepting different inputs.
* Keyword arguments improve readability and reduce mistakes.
* The modulo operator (`%`) is useful for cyclic data such as the alphabet.
* Separating logic into functions makes programs easier to understand and maintain.
* Breaking a large problem into smaller steps makes debugging much easier.

---

## 📌 Future Improvements

* Support uppercase letters while preserving capitalization.
* Allow users to choose custom alphabets.
* Validate invalid shift values automatically.
* Add file encryption and decryption.
* Create a graphical user interface (GUI).
* Save encrypted messages to a text file.
* Improve error handling for invalid user inputs.

---

## 🏁 Conclusion

Day 8 strengthened my understanding of **functions** and how they help organize and simplify code. Learning about parameters and keyword arguments made my functions more flexible, while building the Caesar Cipher project demonstrated how functions, loops, conditionals, string manipulation, and modular programming work together to create a complete application.

This project also reinforced algorithmic thinking by requiring encryption, decryption, alphabet wrap-around using the modulo operator, and continuous program execution through user interaction.