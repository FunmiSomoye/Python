"""
99 Bottles

Create a program that prints out every line to the song "99 bottles of beer on the wall."
Do not use a list for all of the numbers, 
and do not manually type them all in. 
Use a built in function instead.
Besides the phrase "take one down," 
you may not type in any numbers/names of numbers directly into your song lyrics.
Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

Lyrics sample here: https://lyricsplayground.com/alpha/songs/numbers/99bottlesofbeeronthewall.html
Another here: http://www2.hawaii.edu/~pager/313old/AN%20EXERCISE%20IN%20LANGUAGE%20COMPARISONS.htm
""" 

# num_to_words code example from https://stackoverflow.com/questions/19504350/how-to-convert-numbers-to-words-without-using-num2word-library

# create a dictionary for basic number:word pairs
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


# function to pass bottle or bottles
# helps to save space in print statement   
def singular_plural(count):
    return "{}".format("bottle" if (count==1) else "bottles")


# print out the song
def print_song():
    count = 99 # count starts from one hundred
    stop = 0
    step = -1 # decrease count of for loop
    for i in range(count, stop, step):
        num_bottles = num_to_words(i) # pass while loop value to num_to_words function
        num_bottles_left = num_to_words(i-1) # variable useful for the last line of the song lyrics
        """
        one line if then statements used to set conditions 
        for lines of the lyrics that are sensitive to the number
        """
        # print statement for song lyrics
        print(" {} ".format(num_bottles) 
            + singular_plural(i) + # bottle or bottles
            " of beer on the wall,\n {} ".format(num_bottles) # end of first line 
            + singular_plural(i) + # bottle or bottles
            " of beer!\n Take one down,\n Pass it around,\n" # end of second line
            + (" No more bottles of beer on the wall\n\n" if i==1 else (" {} ".format(num_bottles_left)# handle last stanza
            + ("bottle" if (num_bottles_left=='One') else "bottles") 
            + " of beer on the wall!\n\n"))) 
    # last stanza
    print (f" No more bottles of beer on the wall, no more bottles of beer.\n Go to the store and buy some more, {count} bottles of beer on the wall.")


print_song()