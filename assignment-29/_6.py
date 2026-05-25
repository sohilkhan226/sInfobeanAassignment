# 6.
# AI Voice-to-Text Correction System

# A company has developed an AI-based voice-to-text application for virtual meetings.

# Due to microphone disturbances and speech recognition delays, some words are captured multiple times consecutively in the generated text.

# Before saving the meeting transcript, the system must remove duplicate words while maintaining the original order of words.

# Write a Python program to remove repeated words from a sentence.

# Input:
# hello hello team team meeting meeting started
# Output:
# hello team meeting started

sentence = input("Enter sentence: ")

words = sentence.split()
result = []

for word in words:
    if len(result) == 0 or word != result[-1]:
        result.append(word)

text = " ".join(result)
print("After removing duplicates:", text)