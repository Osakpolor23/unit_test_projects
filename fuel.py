# define the main function
def main():
    # prompt the user for a fraction
    fraction = input("Fraction: ").strip()
    # convert the fraction with the convert function
    percentage = convert(fraction)
    # get the fuel guage using the guage function
    fuel_level = gauge(percentage)
    # print fuel level
    print(fuel_level)


# define the get_gauge function to take in a parameter
def convert(fraction):
    try:
        # split the fraction input into the parts
        parts = fraction.split("/")

        # assign the component parts to x and y and map to int
        x, y = map(int, parts)
        # ensure the denominator is not zero
        if y == 0:
            # raise ZeroDivisionError if it is
            raise ZeroDivisionError
        # ensure the numerator is not greater than the denominator
        if x > y:
            # raise ValueError if it is
            raise ValueError
        # return percentage if the aboved conditions are met
        if x <= y and y !=0:
        # Carry out the division, convert to a percentage and round to the nearest whole number
            percentage = round((x / y) * 100)
            return percentage
        
    # catch every ValueError and ZeroDivisionError i.e from int() and dividing numerator by zero
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
            
            
# define the gauge function to take in percentage as a parameter
def gauge(percentage):
     # fulfil the various conditions and return the outputs
    if percentage <= 1:
        return "E"  # E for Empty
    elif percentage >= 99:
        return "F"  # F for Full
    else:
        return f"{percentage}%" # return the percentage unchanged
    
# call the main function to execute the program
if __name__ == "__main__":
    main()
