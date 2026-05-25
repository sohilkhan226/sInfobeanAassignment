# # 7. Enterprise Password Pattern Strength Analyzer

# A cybersecurity company wants to validate advanced passwords.

# ## Conditions:

# * Minimum 10 characters
# * At least:

#   * 1 uppercase letter
#   * 1 lowercase letter
#   * 1 digit
#   * 1 special character
# * No consecutive repeating characters
# * No spaces allowed

# ### Input:

# ```text
# Pyth@n1234
# ```

# ### Output:

# ```text
# Strong Password
# ```

# ### Input:

# ```text
# Paaass@12
# ```

# ### Output:

# ```text
# Weak Password
# ```

# ---


password = input()

has_upper = False
has_lower = False
has_digit = False
has_special = False
has_space = False
has_consecutive = False

special_chars = "@#$%&*!_-"

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True
    if ch in special_chars:
        has_special = True
    if ch == " ":
        has_space = True

for i in range(len(password) - 1):
    if password[i] == password[i+1]:
        has_consecutive = True
        break

if (len(password) >= 10 and has_upper and has_lower and
    has_digit and has_special and not has_space and
    not has_consecutive):
    print("Strong Password")
else:
    print("Weak Password")