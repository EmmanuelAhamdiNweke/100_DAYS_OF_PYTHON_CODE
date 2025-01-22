
# Welcome Message Generator
from datetime import datetime
current_time = datetime.now()
hour = current_time.hour

# Step1: Ask for user details
name = input("what's your name? ").capitalize()
hobby = input("what's your favorite hobby? ")

if hour >= 5 and hour < 12:
    greeting = "Good morning"
elif hour >= 12 and hour < 16:
    greeting = "Good afternoon"
elif hour >= 16 and hour < 22:
    greeting = "Good evening"
else:
    greeting = "Good night"     
print(hour)
# Step 2: Generate a personalized welcome message
print("\n--- Welcome Message ---")
print(f"{greeting}, {name}! ")
print(f"Welcome to the World of Python Programming,")
print(f"It's great to know that you love {hobby}.")
print(f"Get ready to build something amazing today.")
