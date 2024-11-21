# List of names to search through
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user to type the name they want, removing any extra spaces.
search_the_name = input("Please enter the name you want to search for: ").strip()

# Flag to monitor if the name appears in the search results
found = False

# Loop through each name in the list to check if it matches the user's input
for name in names:
    # Convert both names to lowercase to ensure the search is case-insensitive
    if name.lower() == search_the_name.lower():
        # Set 'found' to True and notify the user if a match is discovered.
        found = True
        print(f"Great news! '{search_the_name}' is in the list.")
        break  # Exit the loop early since we found the name

# If the loop completes and the name wasn't found, let the user know
if not found:
    print(f"Sorry, '{search_the_name}' is not in the list.")

    print(f"Sorry, '{search_the_name}' is not in the list.")
