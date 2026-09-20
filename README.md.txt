#Technology Password Strength Checker
A simple python project that checks some basic properties of a password and gives a strength result.

## Features
- Takes a password as input 
- Checks for numbers
- Checks for uppercase letters
- Gives a password strength result

## Technologies used
- Python 3
- String handling
- Conditions
- Basic python functions

## How it works
the program takes a password from the user and checks its length,
number and uppercase letters.

It then uses these checks to give a basic strength result.

## Project Output
The output screenshort is included as:
                                                                 password_checker_output.png

##Challenges & Mistakes I Faced
is project ko banate waqt mujhe kuch galtiyan aur learnings mili:

*** Indentation Issue: ** 
main print("Password Strength:", strength) line ko else: block ke ander likh raha tha ,
jiski wajah se 'Strong' ya 'Medium' Password par result print nahi ho raha tha, isko unindent (picche) karke fix kiya.

* **Typo Errors:**
method name me isupper( ), ki jagah 'isuppuer( )' aur variable me 'password_length' ki jagah 'password_lenghth likh diya tha,
jisse 'Attribute-error' aaya.

##Purpose
I made this project to practice python string handling and learn how programming can be used,
for a simple technology-related task.
