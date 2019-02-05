"""
This will a simple password generator
Will ask user to generate passwrod weak medium and strong
Depending on that it will give a password
"""


import string
import random

def strong_Pass(length = 8):
	everything = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
	password = random.sample(everything,length)
	random.shuffle(password)
	for i in password:
		password = ''.join(password)
	return password
	
def medium_Pass(length = 8):
	everything = string.ascii_uppercase + string.ascii_lowercase + string.digits
	password = random.sample(everything,length)
	random.shuffle(password)
	for i in password:
		password = ''.join(password)
	return password
	
def weak_Pass(length = 8):
	everything = string.ascii_uppercase + string.ascii_lowercase
	password = random.sample(everything,length)
	random.shuffle(password)
	for i in password:
		password = ''.join(password)
	return password
	
def main():
    response = input("Would you like to create a weak, medium or strong password?\n")
	length = int(input("please enter the length of the password "))
    if response.lower() == "weak":
        print("Your password is: " + weak_Pass(length))
    elif response.lower() == "medium":
       print("Your password is: " + medium_Pass(length))
    elif response.lower() == "strong":
        print("Your password is: " + strong_Pass(length))
    else:
        print("please enter one of the above 3 choices")

main()