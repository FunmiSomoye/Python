"""
99 Bottles

Create a program that prints out every line to the song "99 bottles of beer on the wall."
Do not use a list for all of the numbers, 
and do not manually type them all in. 
Use a built in function instead.
Besides the phrase "take one down," 
you may not type in any numbers/names of numbers directly into your song lyrics.
Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
""" 


# num_to_words code from https://stackoverflow.com/questions/19504350/how-to-convert-numbers-to-words-without-using-num2word-library

# create a dictionary for the number:word pairs
num_words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 100: 'One-hundred', 0: 'Zero'}

# function to convert numbers to their words equivalent  
def num_to_words(num):
    if num in num_words:
        in_words = num_words[num]
    else:   
        in_words = num_words[num-num%10] + "-" + num_words[num%10].lower()
    return in_words

# print out the song
def print_song():
    stop = 0 
    i = 100 # count starts from one hundred
    while (i > stop): # while loop stops at 1
        number = num_to_words(i) # pass while loop value to num_to_words function
        x = num_to_words(i-1) # variable useful for the last line
       
        print(" {} ".format(number) 
            + singular_plural(i) + 
            " of beer on the wall,\n {} ".format(number) 
            + singular_plural(i) + 
            " of beer!\n Take one down,\n Pass it around,\n" 
            + (" No more bottles of beer on the wall\n\n" if i==1 else (" {} ".format(x) + ("bottle" if (x=='One') else "bottles") + " of beer on the wall!\n\n"))) # one line if else statements

        i -= 1 # decrease count of while loop

# function to pass bottle or bottles
# helps to save space in print statement   
def singular_plural(count):
    return "{}".format("bottle" if (count==1) else "bottles")


print_song()