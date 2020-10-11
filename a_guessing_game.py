# imports
from random import seed # to ensure that your code produces the same result each time
from random import randint # so to generate only integer values
import sys


# initial values
game_on = False

# try a while loop
def run_game():

    global game_on
   # game_on = game_on

    while game_on:
        count = 0
        max_guesses = 10

        while count < max_guesses:
            compare_values(validate_number_input(), computer)
            count += 1  

        print("\nYou have exceeded the maximum of {} guesses".format(max_guesses))
        game_on = False
        print("\nWould you like to play again?")
        switch_on_game() #switch on the game


# function to validate user input
def validate_number_input():
     
    global user_input

    while True: 
        try: 
            user_input = input("\nEnter a 'whole number' ")
            user_input = int(user_input)
            
            if user_input > 20:
                print("\nPlease enter a number less than 20.")
                continue
            return user_input

        except ValueError:
            print("\nPlease enter positive whole numbers only, no letters or decimals either.")
            continue
    


# function to switch game on or off
def switch_on_game():
    global game_on
    while True:
        try:
            valid_response = ['yes', 'no']
            game_play = input("Yes or No ?")
            game_play = game_play.lower()
            
            if (not game_play.isalpha()):
                print("Type in alphabets ('Yes' or 'No') ")
                continue
            
            elif (game_play not in valid_response):
                print("Please type in 'Yes' or 'No'")
                continue

            else:
                if game_play == "yes":
                    game_on = True
                    print("\nWe hope you win the computer :)")
                    run_game()
                else:
                    print("Goodbye")
                    sys.exit()

        except ValueError:
            print("\nPlease enter 'Yes' or 'No'.")
            continue


# function to compare the numbers
def compare_values(user, computer):
    if user < computer:
        print("\nAwww, your guess is too low!")
        #print("\nThe computer generated number {}".format(computer))
    elif user == computer:
        print("\nAwesome! You guessed correctly!!!")
        print("\nWould you like to play again?")
        switch_on_game()
    else:
       print("\nYour guess is too high! Haha!")
       #print("\nThe computer generated number {}".format(computer))
    #return result


# program start
print("Welcome to the Guessing Program \nYou have a maximum of 10 guesses")

# init
#seed(1) # seed the random number generator to increase predictability during testing
computer = randint(0, 20)

# let the game begin
print("\nAre you ready to start?") 
switch_on_game()












