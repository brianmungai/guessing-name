#this program demonstrates a guessing game

from random import randint

# get user name
user_name = input("what's your name?")
print("hello there " + user_name + "!")

# generate a random number
random_number = randint (10,50)

counter = 0
while counter < 5:
    user_number = eval (input ("enter a number"))
    counter += 1

    if user_number < random_number:
        print("ÿour guess is too low try again")
    elif user_number > random_number:
        print("your guess is too high try again")
    elif user_number == random_number:
   
        break
print ("game over.")
if user_number == random_number :
    print ("you win")
elif user_number < random_number:
    print ("the correct number was" , random_number)
elif user_number > random_number :
    print ("the correct number was" , random_number)










# get user number
# generate a random number 
# using a while loop
# check if user input is equal to generate number