"""
A She Code Africa Mentorship assignment

Password Generator: 
Write a program, which generates a random password for the user. 
Ask the user how long they want their password to be, 
and how many letters and numbers they want in their password. 
Have a mix of upper and lowercase letters, 
as well as numbers and symbols. 
The password should be a minimum of 6 characters long.
"""

import secrets # use secrets as it is said to be cryptographically safer than random 
import string # import string module
import random # import random module

# Define Functions

# function for main program
def main():
    # Action
    validate_number_input() # run function to validate user input
    print("\nHere is your password: ", generate_strong_password(length, num_letters)) # run function to generate secure password and print result

# function to validate the user's input
def validate_number_input():
    while True:

        global length, num_letters # declare as global variables so they can be reused outside the function

        try: # use try except to validate user input
            length = input("How long do you want your password to be (character length)?") # length of password
            num_letters = input("How many alphabets do you want in your password?") # number of alphabets in password
            
            length = int(length) # attempt to convert the user input to an integer
            num_letters = int(num_letters) # attempt to convert the user input to an integer
        
            if length < 6:
                print("\nPlease enter a number greater than 6 for the length of your password.")
                continue

        except ValueError:
            print("\nPlease enter positive whole numbers only, no letters or decimals.")
            continue

        break

# function to generate the secure password
def generate_strong_password(length, letters):
    space_left = length - letters # get a figure for how many integers and symbols to be in the password
    num_or_symbol = int(space_left/2) # set new variable for number of integer strings and symbols

    # generate strings, both upper and lower case
    password_raw = ''.join(secrets.SystemRandom().choice(string.ascii_letters) for _ in range(letters)) # include SystemRandom() for cryptographic safety
    # generate digits as string too using and join to password
    password_raw += ''.join(secrets.SystemRandom().choice(string.digits) for _ in range(num_or_symbol)) # join each randomly generated with no separator to existing variable
    # generate symbols and joint to password
    password_raw += ''.join(secrets.SystemRandom().choice(string.punctuation) for _ in range(num_or_symbol)) # join each randomly generated with no separator to existing variable

    # shuffle the randomly generated characters
    password_list = list(password_raw) # make password a list
    random.shuffle(password_list) # shuffle the new list
    password = ''.join(password_list) # unpack the shuffled list and save as a new variable
    return password

# start the program
main()