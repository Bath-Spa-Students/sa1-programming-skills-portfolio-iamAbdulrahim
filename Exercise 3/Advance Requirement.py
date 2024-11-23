# Function to check if Its a even or odd number
def check_even_odd(number):
    #  even if the number is evenly divisible by two.
    if number % 2 == 0:
        return f"{number} is even."
    else:
        # If not, it is an odd number
        return f"{number} is odd."

#The main function is to process user input and show the outcome.
def main():
    # Ask the user to input  a number
    try:
        users_number = int(input("Please enter a number: "))
        # Get the outcome message by asking the check_even_odd function.
        result_message = check_even_odd(users_number)
        # Print the result message
        print(result_message)
    except ValueError:
        # it Shows an error message if the user inputs a value which is not  an integer.
        print("Invalid input. Please enter a numerical value.")

# Only run the main function if this script is run directly
if __name__ == "__main__":
    main()
    
