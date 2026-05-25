# 3.
# Word Counter in Complaint Message

# A customer care system wants to count how many words are present in a complaint message.

# Input:
# Enter complaint: Delivery was delayed again today

# Output:
# Total words: 5


complaint = input("Enter complaint: ")

count = 0
in_word = False

for ch in complaint:
    if ch != " ":
        if not in_word:
            count += 1
            in_word = True
    else:
        in_word = False

print("Total words:", count)