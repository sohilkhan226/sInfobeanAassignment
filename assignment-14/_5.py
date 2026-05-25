# 5.Number Stability Analyzer

# A science lab studies whether digits are in increasing order.

# Write a program using for-else loop:

# - If every next digit is greater than previous print Stable Number
# - Else Unstable Number

# Input:
# 12359

# Output:
# Stable Number

num_str = input()

for i in range(len(num_str) - 1):
    if int(num_str[i]) >= int(num_str[i+1]):
        print("Unstable Number")
        break
else:  # Executes only if no break occurs
    print("Stable Number")

'''
num = int(input("Enter number: "))

# मान लेते हैं कि नंबर Stable है
is_stable = True

# नंबर के आखरी दो अंकों को आपस में तुलना करने के लिए लूप
while num > 9:
    last_digit = num % 10          # सबसे आखरी अंक
    prev_digit = (num // 10) % 10  # उसके ठीक पहले वाला (Adjacent) अंक
    
    # पीछे से चेक कर रहे हैं, इसलिए पहले वाला अंक हमेशा छोटे वाले से छोटा होना चाहिए
    # अगर पहले वाला अंक बड़ा या बराबर निकला, तो नियम टूट गया
    if prev_digit >= last_digit:
        is_stable = False
        break
        
    num = num // 10  # आखरी अंक को हटाकर नंबर छोटा करें

# फाइनल रिजल्ट प्रिंट करें
if is_stable:
    print("Stable Number")
else:
    print("Unstable Number")

'''




#
# num_str = input()

# i = 0
# stable = True

# while i < len(num_str) - 1:
#     if int(num_str[i]) >= int(num_str[i + 1]):
#         print("Unstable Number")
#         stable = False
#         break
#     i += 1

# if stable:
#     print("Stable Number")