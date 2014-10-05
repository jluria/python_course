def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "That is not a valid input!"
    return number

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock" 
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "That is not a valid number!"
    return name


import random    

def rpsls(player_choice): 

    print ""
    
    print "Player chooses", player_choice
    
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 4)
    comp_choice = number_to_name(comp_number)
    
    print "Computer chooses", comp_choice
        
    def difference(player_number, comp_number):
        difference = (player_number - comp_number) % 5
        return difference
    
    if difference(player_number, comp_number) == 1:
        print "Player wins!"
    elif difference(player_number, comp_number) == 2:
        print "Player wins!"
    elif difference(player_number, comp_number) == 3:
        print "Computer wins!"
    elif difference(player_number, comp_number) == 4:
        print "Computer wins!"
    else:
        print "Unbelievable... It's a tie!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
