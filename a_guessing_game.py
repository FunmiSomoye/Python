"""
A She Code Africa Mentorship assignment

Guess The Number: 
Write a program where the computer randomly generates a number between 0 and 20. 
The user needs to guess what the number is. 
If the user guesses wrong, 
tell them their guess is either too high, or too low. 
"""

# imports
#from random import seed # to ensure that your code produces the same result each time
from random import randint # so to generate only integer values
import sys # import system module


game_on = False # initialise game_on as False

# function for main program
def main():
    # welcome message
    print("Welcome to the Guessing Program")

    # instructions
    print("Your computer would generate random numbers between 0 and 20. \nYou are to guess what number your computer generates. \nYou have a maximum of 10 guesses in one round")

    # init
    #seed(1) # seed the random number generator to increase predictability during testing
    
    # computer to generate random integers between 0 and 20
    global computer # declare as a global variable
    computer = randint(0, 20) 

    # let the game begin
    print("\nAre you ready to start?") # print on a new line
    switch_on_game() # run the function to switch on the game


# function to switch game on or off
def switch_on_game():
    global game_on # declare as a global variable
    while True:
        #try: # try exceptions
            valid_response = ["yes", "no"] # set what a valid response looks like
            game_play = input("Yes or No ?") # receive the user input
            game_play = game_play.lower() # set user input to lower case letters
            
            # check if user input is a string
            if (not game_play.isalpha()): 
                print("Type in alphabets ('Yes' or 'No') ")
            
            # confirm that user entered yes or no
            elif (game_play not in valid_response): 
                print("Please type in 'Yes' or 'No'")

            else:
                # if Yes
                if game_play == "yes": 
                    game_on = True # initialise game_on as True
                    print("\nWe hope you win the computer :)")
                    run_game() # run the function to make the game run
                    break # don't come back in here
                
                # if No
                else:
                    print("Goodbye")
                    sys.exit() # exit the program
    
        #except ValueError: # raise a value error 
           # print("\nPlease enter 'Yes' or 'No'.")
            #continue


# function to run the game
def run_game():

    global game_on # declare as a global variable
   # game_on = game_on

    while game_on: 
        count = 0 # initialise count to monitor While loop
        max_guesses = 10 # set maximum number of guesses to 10

        while count < max_guesses:
            # run the function to compare User guesses with Computer generated numbers
            compare_values(validate_number_input(), computer) # run the compare values function
            count += 1 # increase count

        print("\nYou have exceeded the maximum of {} guesses".format(max_guesses))
        game_on = False # set game_on to False because maximum number of guesses has been exited

        # give the user an option to play again if they want to play again
        print("\nWould you like to play again?")
        switch_on_game() # run function to switch on the game


# function to validate user input
def validate_number_input():
     
    global user_input # declare as global variable

    while True: 
        try: # use try except to validate user input
            user_input = input("\nEnter a 'whole number' ") # receive the user input
            user_input = int(user_input) # attempt to convert the user input to an integer
            
            if user_input > 20: 
                print("\nPlease enter a number less than 20.")
                continue # continue to the next line
            return user_input # save user_input value into the function for future use

        except ValueError: # raise a value error if input is not an integer
            print("\nPlease enter positive whole numbers only, no letters or decimals either.")


# function to compare the User value to the computer geenrated value
def compare_values(user, computer):
    if user < computer:
        print("\nAwww, your guess is too low!")
        #print("\nThe computer generated number {}".format(computer)) # uncomment for testing
    elif user == computer:
        print("\nAwesome! You guessed correctly!!!")
        print("\nWould you like to play again?")
        switch_on_game() # run the function to switch on the game
    else:
       print("\nYour guess is too high! Haha!")
       #print("\nThe computer generated number {}".format(computer)) # uncomment for testing
    

# start the program
main()











