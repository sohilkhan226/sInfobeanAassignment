# QNo 8:--
# SMART TEXT PROCESSING SYSTEM

# A software company is developing a Smart Text Processing System for
# handling user messages. Different users require different text
# transformations. To avoid creating separate applications, the company
# wants a menu-driven program where users can select operations according
# to their requirements.

# The system should continue executing until the user selects Exit.

# ====================================================== MENU
# ======================================================

# ===== Smart Text Processing System =====

# 1.  Reverse Complete String
# 2.  Reverse Every Word
# 3.  Reverse Word Order
# 4.  Exit

# ====================================================== Choice 1 :

# Conditions: - Reverse the complete string - Ignore extra spaces - Keep
# special characters (@,#,$,%) in their original positions - Do not use
# built-in reverse functions

# Example: Input: ja@va#py

# Output: yp@av#aj

# Test Case 1: ab@cd#ef Output: fe@dc#ba

# Test Case 2: py@th#on Output: no@ht#yp

# Test Case 3: java@proOutput : orpa@vaj

# ====================================================== Choice 2 :

# Conditions: - Reverse every word separately - Words containing digits
# should not be reversed - Ignore extra spaces between words - First
# letter of each reversed word should become uppercase

# Example: Input: java is easy123 programming

# Output: Avaj Si easy123 Gnimmargorp

# Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22
# Repoleved

# Test Case 2: hello java99 world Output: Olleh java99 Dlrow

# ====================================================== Choice 3 :

# Conditions: - Reverse order of words - Remove duplicate words - Ignore
# case while checking duplicates - Keep only first occurrence

# Example: Input: Java python Java react Python

# Output: React Python Java

# Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML

# Test Case 2: Python React Java Python React Output: Java React Python

# ====================================================== Choice 4
# ======================================================

# Program Closed Successfully


while True:
    print("\n===== Smart Text Processing System =====")
    print("1. Reverse Complete String")
    print("2. Reverse Every Word")
    print("3. Reverse Word Order")
    print("4. Exit")

    choice = input("Enter choice: ")

    # ========================================
    if choice == "1":
        text = input("Enter text: ")

        letters = []
        for ch in text:
            if ch not in "@#$%":
                letters.append(ch)

        reversed_letters = ""
        for i in range(len(letters)-1, -1, -1):
            reversed_letters += letters[i]

        result = ""
        index = 0
        for ch in text:
            if ch in "@#$%":
                result += ch
            else:
                result += reversed_letters[index]
                index += 1

        print("Output:", result)

    # ========================================
    elif choice == "2":
        text = input("Enter text: ")

        words = text.split()
        result = ""

        for word in words:
            has_digit = False
            for ch in word:
                if ch.isdigit():
                    has_digit = True
                    break

            if has_digit:
                result += word + " "
            else:
                rev = ""
                for ch in word:
                    rev = ch + rev
                rev = rev[0].upper() + rev[1:]
                result += rev + " "

        print("Output:", result.strip())

    # ========================================
    elif choice == "3":
        text = input("Enter text: ")

        words = text.split()
        unique = []

        for word in words:
            lower_word = word.lower()
            if lower_word not in [w.lower() for w in unique]:
                unique.append(word)

        result = ""
        for i in range(len(unique)-1, -1, -1):
            result += unique[i] + " "

        print("Output:", result.strip())

    # ========================================
    elif choice == "4":
        print("Program Closed Successfully")
        break

    else:
        print("Invalid Choice")