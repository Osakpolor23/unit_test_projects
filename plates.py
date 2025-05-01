# Define a function to validate license plates
def main():
    # prompt the user for a license plate, convert it to uppercase and validate it
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# define a function to check if the license plate is valid and return a boolean value
def is_valid(plate):
    # check if the length of the plate is between 2 and 6 characters
    if not 2 <= len(plate) <= 6:
        return False
    
    # check if the first two characters are letters
    if not plate[0:2].isalpha():
        return False
   
    # Track if the numbers have started
    number_started = False # assign a default False flag to track where the number started

    for i, char in enumerate(plate):  # iterate through the plate, keeping track of the index(i) and character

        # check if the character is a digit
        if char.isdigit():  
          
            if not number_started: # To change the flag to True when a digit is found
                # Check the first digit isn't 0
                if char == "0":
                    return False
                number_started = True # update the flag to True once a digit is found

            # check if all remaining characters are digits
            elif not plate[i:].isdigit():
                return False
            
        # check if letters are found after the digits
        elif number_started:  # check if number was previously found, return False as it's invalid
            return False
        
    # check if spaces and special characters are not used
    if not plate.isalnum():
        return False
    
    # if all checks are passed, return True
    return True

# call the main function to execute the program
if __name__ == "__main__":
    main()

    