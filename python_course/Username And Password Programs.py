# Username Validation:
username= input("Enter a username: ")
if len(username)>=8 and not username[0].isdigit():
    print("The username", username, " is valid.")
else:
    print("The username", username, " is not valid.")

# Email Domain Extraction:
email= input("Enter an email address: ")
index = email.find('@')
if index != -1:
    domain_part = email[index + 1:]
    print("Email domain is:", domain_part)
else:
    print("Invalid Email Awddress.")

# Password Strength Checker:
password= input("Enter password: ")
length= len(password)>=8
upper= False
lower= False
number= False
for char in password:
    if char.isupper():
        upper = True
    elif char.islower():
        lower = True
    elif char.isdigit():
        number = True
if length and upper and lower and number:
    print("Password Strength: Strong.")
elif length and (upper or lower or number):
    print("Password Strength: Moderate.")
else:
    print("Password Strength: Weak.")

# #Character Frequency Counter:
string = input("Enter a word: ")
print("Character frequencies:")
for char in string:
    count = string.count(char)
    print(f"{char}: {count}")

