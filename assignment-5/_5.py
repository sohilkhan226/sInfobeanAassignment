# 5. Banking Security System
#    A bank validates login attempt:

# * If username is "admin" → Valid user
# * If password length ≥ 8 → Strong password

# Input:
# Enter username: admin
# Enter password: secure123

# Output:
# Valid user
# Strong password

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    print("Valid user")

if len(password) >= 8:
    print("Strong password")


# username= input("enter the username")
# password= input("enter the password")      

# if username.lower() == "admin":
#     if len(password)>=8:             //hum "len()" ka use sting,list,tupple,dictonary me karte 
#         if int(password)==56217867:  //password string thi islie hamne password ko integer kar
#             print("login h")
#         else:
#             print("wrong password")
#     else:
#         print("weak password")
# else:
#     print("not valid user")