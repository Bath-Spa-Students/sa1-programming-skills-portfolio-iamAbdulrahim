# Define the correct password for the system
correct_password = "12345"

# Setting  the maximum number of allowed password attempts
max_attempts = 5

# Initialize a counter to keep track of the number of attempts made
attempts = 0

# Creating a loop that keeps going until the right password is entered or all attempts have been made.
while attempts < max_attempts:
    # Ask the user to enter the password
    user_password = input("Please enter the password: ").strip()
    
    # Mask the entered password with asterisks for privacy
    masked_password = '*' * len(user_password)
    
    # Increase the attempt count by 1 after each entry
    attempts += 1

    # Verify that the password entered corresponds to the one that is stored.
    if user_password == correct_password:
        # If correct, give  access and end the loop
        print("Access granted. Welcome User!")
        break
    else:
        # If incorrect, display an error message along with the masked password
        print(f"Incorrect password: {masked_password}")
        
        # If this is the user's second-to-last try, give them a hint.
        if attempts == max_attempts - 1:
            print("Hint: The password is number.")
        
        # If the user has used all attempts, lock them out and notify them
        if attempts == max_attempts:
            print("Access denied. You have been locked out due to too many incorrect attempts.")
