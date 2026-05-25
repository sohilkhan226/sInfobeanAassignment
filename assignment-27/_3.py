# 3.  Smart Chat Message Cleaner

# A social media company noticed that users often enter messages with
# unnecessary spaces. To improve readability and storage efficiency, the
# system should remove extra spaces and keep only a single space between
# words.

# Input: Enter message: Java is easy

# Output: Cleaned Message: Java is easy

msg = input("Enter message: ")

clean = ""
space_flag = False

for ch in msg:
    if ch == " ":
        if not space_flag:
            clean += ch
            space_flag = True
    else:
        clean += ch
        space_flag = False

print("Cleaned Message:", clean.strip())