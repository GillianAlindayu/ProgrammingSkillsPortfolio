# Chapter 6: exercises 

# Exercise 1: pizza toppings ballot_bos_with_check: 

# Write a loop that prompts the user to enter a series of pizza toppings unti they enter 'quit'value.
# As they enter each topping, print a message saying you'll add that topping to their pozza.

# Python program of pizza toppings 

prompt = "\nWhat topping would you like on our pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True: 
    topping = input(prompt)
    if topping != 'quit': 
        print(f" I'll add {topping} to your pizza.")
    else: 
        break

# Exercise 2: Movie ticket: ballot_box_with-check 

# A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free.
# If they are between 3 and 12, the ticket is $10, and if they are over age 12, the ticket is $15. 
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket. 

prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished."

while True: 
    age = input(prompt)
    if age == 'quit': 
        break 
    age = int(age)

    if age < 3: 
        print("You got in free!")
    elif age < 13: 
        print("Your ticket is $10.")
    else: 
        print("Your ticket is $15.")
        break 
    
# Exercise 3: infinity loop ballot_box_with_check

# Write a loop that never ends, and run it. (To end the loop, press ctrl + C or close t he window displaying the output.) 

#python program infinite loop an example of writing a name 

a = 1 
while a==1: 
    b = ("What's your name?")
    print("hi", b, ", Welcome to programming.")
    break 

# Exercise 4: Deli: ballot_box_with_check: 

# Make a list called sandwich_orders and fill it with the names of various sandwuches.
# Then make a empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order, such as I made tuna sandwich. 
# As each sandwich is made, move it to the list to finish sandwhiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am working with your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches: 
    print(f"I made a {sandwich} sandwich. ")


# Exercise 5: No pastrami ballot_box_with_check: 

# Using the list sandwich_orders from 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all.
# Occurence of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami', 
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I am sorry, we're all run out of pastrami today.")
while 'pastrami' in sandwich_orders: 
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")





