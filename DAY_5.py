# Countdown Timer:

# import time

# # Step 1: Get user input for countdown start
# start = int(input("Enter the number to start the countdwon from: "))

# # Step 2: Countdown using a while Loop
# print("\n--- Countdown Begins ---")
# while start > 0:
#     print(start)
#     time.sleep(2)
#     start -= 1

# # Step 3: Print final message

# print("Countdown Complete")


# Pseudo Code (Step By Step Questions)
# Write a python code that does the following

# Step 1
# Import the Time library

import time

# Step2
# Asks user for input and convert the input to an integer and store in a variable named 'start'

start = int(input("Enter the number to start countdown "))
speed = int(input("Enter speed for countdown "))
halfway = round(start / 2)
print("\n--- Countdown Begins ---")
# Step3
# Write a while loop that check for inputs as long as the input is less than 0

while start > 0:
# Step4
# Print the input(i.e the start variable) for every iteration
    
    print (start)
        
# Step 5
# Using the time library, pause the execution for at least 1 sec
    time.sleep(speed)
# Step 6
# After each iteration, subtract 1 from the start variable.
    start -= 1
    if halfway == start:
        print('halfway')
# Step 7
# Print "Countdown Completed"
print ("Countdown Completed 🎉")
