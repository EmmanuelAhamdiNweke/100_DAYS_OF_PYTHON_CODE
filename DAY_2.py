
# Personalized Greeting Program
from datetime import datetime
current_date = datetime.now()
current_year = current_date.year
birth_year = int(input("What is your year of birth? "))
age = current_year - birth_year

#Step 1: Ask for user details
name = input("What is your name? ")
# age = input("How old are you? ")
color = input("What is your favourite colour? ")

# Step 2: Generate a personalized greeting message
print("\n---- Personalized Greeting ----")
print(f"Hello, {name}!👋")
print(f"You are {age} years old and {color} is a beautiful colour!")
print("Your are now ready to start your python adventure 🚀🐍")