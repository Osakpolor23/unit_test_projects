# Define the main function
def main():
    # prompt user for input and convert to upper case
    user_input = input("Input: ")
    # apply the vowel filter function
    print(shorten(user_input))

# define the function to remove vowels
def shorten(word):
    # assign the vowel letters to a variable 
    vowels = "AEIOU"
    # loop through every character in the string -- a string is iterable like a list
    for char in vowels:
        # replace every character found in vowels both the upper and lower case versions with an empty string
        word = word.replace(char, "").replace(char.lower(), "")
    # return input so as to be used in the function
    return word
        


# call the main function      
if __name__ == "__main__":
    main()