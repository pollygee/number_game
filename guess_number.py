# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random


# initialize global variables
num_range = 100
hidden_number = 0
counter =7



# helper function to start the game
def new_game():
    print "New Game \n"
    range100()
 


# define event handlers for control panel
def range100():
    global hidden_number, counter, num_range
    counter  = 7
    num_rage = 100
    print "Range is from 0 to 100"
    print "You have ", counter, " guesses remaining. \n"
    hidden_number = random.randrange(0, 100)
  
    
# button that changes range to range [0,100) and restarts
def range1000():
    global hidden_number, counter, num_range
    print "Range is from 0 to 1000"
    hidden_number = random.randrange (0, 1000)
    counter = 10
    num_range = 1000
    print "You have ", counter, " guesses remaining.\n"
    
    
# button that changes range to range [0,1000) and restarts
def input_guess(guess):
    global hidden_number, counter, num_range
    guess = int(guess)
    counter = counter -1
    print "Your guess is ", guess
    if counter > 0:
        if guess < hidden_number:
            print "Higher!  Guess again."
            print "You have ", counter, "guesses remaining\n"
        elif guess > hidden_number:
            print "Lower!  Guess again."
            print "You have ", counter, "guesses remaining\n"
        else:
            print "You got it!\n" 
            if num_range == 100:
                range100()
            else:
                range1000()
        
    else:
        print "Game Over!  Try again \n"
        if num_range == 100:
            range100()
        else:
            range1000()
    
   
# creates frame
f= simplegui.create_frame("Guess the Number", 200, 200)

#registers handlers
f.add_button("Range is (0, 100]", range100, 200)
f.add_button("Range is (0, 1000]", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)



# call new_game and start frame
new_game()

