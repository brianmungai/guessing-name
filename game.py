#this program demonstrates a guessing game

from random import randint

#1. get user name
user_name = input("what's your name?")
print("hello there " + "user_name " + "!")

# generate a random number
number = randint (10,50)

counter = 0
while counter < 5:
    user_number = eval (input ("enter a number"))

#2. get user number
# generate a random number 
# using a while loop
#check if user input is equal to generate number