# Basic requirements.
#Requiring the user to enter the response.
answer = input("What is the capital of France? ").strip()
#For checking the output.
if answer.lower() == "paris":
    print("Correct! The answer is Paris.")
else:
    print("Incorrect. The correct answer is Paris.")

# Advanced requirements.
# The Quiz.
questions = {
    "France": "Paris",
    "Albania": "Tirana",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Georgia": "Tbilisi",
    "Belgium": "Brussels",
    "Ireland": "Dublin",
    "Norway": "Oslo",
    "Turkey": "Ankara"
}
#For counting score.    
score = 0
#For asking questions and reviewing the output.  
for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ").strip()
    if answer.lower() == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {capital}.")
    
    print(f"\nYour final score: {score}/{len(questions)}")
