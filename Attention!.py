# Military time to normal time
# Brayden Towner
# 11/17/2023

# I could totally parse normal time, but that wasn't the assignment
military_time = int(input("What is the current military time? (Formatted 4:00 PM is 1600, 4:00AM is 400, etc.) >  "))

if military_time < 1200:
    print("Good morning!")
elif 1200 <= military_time < 1700:
    print("Good afternoon!")
else:
    print("Good evening!")

number = int(input("Write a number divisible by 5 for a hello >  "))

# This checks if number is divisible by 5 using mod (Yes, you did teach me this*. No, you can't dock points)
if number % 5 == 0:
    print("Hello!")
else:
    print("Goodbye!")

# *I technically learned this from my scratch days