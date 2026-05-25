2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST

name = input("Enter employee name: ")

short_id = ""
new_word = True

for ch in name:
    if ch == " ":
        new_word = True
    else:
        if new_word:
            short_id += ch.upper()
            new_word = False

print("Employee Short ID:", short_id)