# Define the function
def main():
    # prompt the user for the greeting
    greeting = input("Greeting:  ").strip().lower()
    # get the value of the greeting
    greet_value = value(greeting)
    print(greet_value)

    

def value(greeting):
    # ensure case insensitivity and remove whitespaces
    greeting = greeting.lower().strip()
    # check the prefix the greeting starts with
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    # if the prefix starts with something else
    else:
        return 100


# call the main function
if __name__ == "__main__":
    main()
