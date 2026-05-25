# 2. Reverse Sentence + Reverse Each Word

# Secret Military Communication Decoder
# A defense organization stores highly confidential messages in encrypted form.
# To decode the message:

# 1. Reverse the entire sentence.
# 2. Reverse every individual word.
# 3. Store the final result back into the original string variable.

# You must use the split() method.
# Input:

# ```
# Python is powerful
# ```

# Output:

# ```
# lufrewop si nohtyP
# ```


text = input()

# Step 1: Reverse complete sentence
rev_sentence = text[::-1]

# Step 2: Reverse each word
words = rev_sentence.split()
final = ""

for word in words:
    final += word[::-1] + " "

text = final.strip()
print(text)