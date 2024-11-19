# Define variables for personal information
name = "Abdul Rahim"  # Name as a string
hometown = "Pakistan"    # Hometown as a string
age = 17                 # Age as an integer

# Keeping data in a dictionary using descriptive keys.
info = {
    "Name": name,        # Key "Name" with name as its value
    "Hometown": hometown, # Key "Hometown" with hometown as its value
    "Age": age            # Key "Age" with the value of age
}

# Print each piece of information on a new line
print(f"{info['Name']}\n{info['Hometown']}\n{info['Age']}")
