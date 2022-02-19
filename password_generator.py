# This file creAates a password of you desired format

import string
import secrets

def strong_pass(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))

def med_pass(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))
    
def weak_pass(length):
    alphabet = string.ascii_letters
    return ''.join(secrets.choice(alphabet) for i in range(length))

################################################

print("Password Generator:\n")

len_pass = input("How long should your password be? ")
len_pass = int(len_pass)

form_pass = ""
poss_form = ["Strong", "strong", "S", "s", "Medium", "medium", "M", "m", "Weak", "weak", "W", "w"]
strong = ["Strong", "strong", "S", "s"]
medium = ["Medium", "medium", "M", "m"]
weak = ["Weak", "weak", "W", "w"]
password = ""


while True:
    print("\nWhich format would you like?")
    form_pass = input("Strong, Medium, Weak\n\n")
    if form_pass in poss_form:
        break
    else:
        continue

if form_pass in strong:
    password = strong_pass(len_pass)
elif form_pass in medium:
    password = med_pass(len_pass)
else:
    password = weak_pass(len_pass)

print(password)
