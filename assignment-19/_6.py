# 6.
# Data Validation System – Character Identifier
# A system needs to validate user input characters.
# If the input is:
# Alphabet → display "Alphabet"
# Digit → display "Digit"
# Otherwise → display "Special Character"
# Write a program using inline if to classify the character.


ch = input("Enter a character: ")

result = "Alphabet" if ch.isalpha() else "Digit" if ch.isdigit() else "Special Character"

print(result)