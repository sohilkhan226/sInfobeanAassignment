# Q131: Check if a string is a valid email address.
# Input: S = "test@example.com"
# Output: True
import re
S = "test@example.com"
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
print(bool(re.match(pattern, S)))

