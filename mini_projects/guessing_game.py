# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

secret_number = random.randrange(0, 100)
counter = 7
small_game = True

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, counter   
    range100()

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, counter, small_game
    counter = 7
    secret_number = random.randrange(0, 100)
    small_game = True
    print "New game. The secret number is between 0 and 100."
    print "Number of remaining guesses is 7"
    print ""
    return secret_number, counter

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number, counter, small_game
    counter = 10
    secret_number = random.randrange(0, 1000)
    small_game = False
    print "New game. The secret number is between 0 and 1000."
    print "Number of remaining guesses is 10"
    print ""
    return secret_number, counter
    
def input_guess(guess):
    # main game logic goes here
    global counter
    guess = int(guess)
    if counter > 1:
        counter -= 1
        print "Guess was", guess
        print "number of remaining guesses is", counter
        
        if guess < secret_number:
            print "Higher!"
            print ""
        elif guess > secret_number:
            print "Lower!"
            print ""
        elif guess == secret_number:
            print "Correct!"
            print ""
            if small_game:
                range100()
            else:
                range1000()
        return counter
    elif counter == 1:
        counter -= 1
        print "Guess was", guess
        print "number of remaining guesses is", counter
        if guess == secret_number:
            print "Correct!"
            print ""
            if small_game:
                range100()
            else:
                range1000()
        else:
            print "You ran out of guesses. The number was", secret_number
            print ""
            if small_game:
                range100()
            else:
                range1000()


    
# create frame
frame = simplegui.create_frame("My Frame", 250, 250)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
inp = frame.add_input("Guess the number", input_guess, 200)

frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
