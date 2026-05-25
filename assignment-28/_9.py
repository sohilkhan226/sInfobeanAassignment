# write a program  to reverse a string or reverse each word
#  but in this program result should be update in orignal string...



text = input("Enter text: ")
rev = ""
for ch in text:
    rev = ch + rev
text = rev

print("Updated String:", text)