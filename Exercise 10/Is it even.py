# Function to check if Its a even or odd number
def check_even_odd(number):
    # It is even if the number is evenly divisible by two.
    if number % 2 == 0:
        return f"{number} is even."
    else:
        # If not, it's odd number
        return f"{number} is odd."

# Main function to handle user input and display the result
def main():
    # Ask the user to enter a number
    try:
        users_number = int(input("Please enter a number: "))
        # Call the check_even_odd function and get the result message
        result_message = check_even_odd(users_number)
        # Print the result message
        print(result_message)
    except ValueError:
        # Show an error message if the user inputs a value that isn't an integer.
        print("Invalid input. Please enter a numerical value.")

# Only run the main function if this script is run directly
if __name__ == "__main__":
    main()
    
