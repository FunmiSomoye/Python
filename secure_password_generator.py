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
import string
import random

# Define Functions
def validate_number_input():
    while True:
        global length, num_letters
        try:
            length = input("How long do you want your password to be (character length)?")
            num_letters = input("How many characters should be made of letters in the password?")
            
            length = int(length)
            num_letters = int(num_letters)
        
            if length < 6:
                print("\nPlease enter a number greater than 6 for the length of your password.")
                continue

        except ValueError:
            print("\nPlease enter positive whole numbers only, no letters or decimals.")
            continue

        break


def generate_strong_password(length, letters):
    difference = length - letters
    count = int(difference/2)
    password = ''.join(secrets.SystemRandom().choice(string.ascii_letters) for _ in range(letters)) #include SystemRandom() for cryptographic safety
    password += ''.join(secrets.SystemRandom().choice(string.digits) for _ in range(count))
    password += ''.join(secrets.SystemRandom().choice(string.punctuation) for _ in range(count))

    # shuffle the randomly generated characters
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password


def main():
    # Action
    validate_number_input()
    print("\nHere is your password: ", generate_strong_password(length, num_letters))


main()