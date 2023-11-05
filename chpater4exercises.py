#Chapter 4: Exercises

# Exercise 1: Alien colors #1 ballot_box_with_check: 

    #Imagine an alien just shut down in a game. Create a variable called alien_color that assign it a value of 'green', 'yellow', or 'red'
    #Write if an statement whether the alien's color is green, if it is, print a message that the player just earned five points. 
    #Write one version of this program that passes that if test and another that fails. (The version that fails will have no output )

#passing version 
#alien_colors_1.py

alien_color = 'green'

if alien_color == 'green': 
    print('You just earned 5 points')

#Failing version 
#alien_colors_1_fail.py 

alien_color = 'red'
                                                                                                                                                                      
if alien_color == 'green':
    print("You just earned 5 points!")

#Exercise 2: alien colors #2 ballot_box_with_check:

#Choose a color for an alien you did in exercise 5-3 and write an if-else chain. 
    # If the alien color is green, the statement that the player just earned 5 points for shooting an alien 
    # If the alien color isn't green, print a statement that the player just earned 10 points. 
    # Write a version of this program that runs if the block and another that runs the else block.

#alien_color_2_if_block_runs.py
 
alien_color = 'Green'
if alien_color == 'green':
    print("You earned 5 points")
else: 
    print("You just earned 10 points")

#alien_color_2_else_block_runs.py 

alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("you just earned 10 points!")

# Exercise 3: Alien colors #3 ballot_box_with_check:

#Turn your if-else chain from exercise 5-4 into an if-elifelse chain.
    # If the alien is green, print a message that the player earned 5 points.
    # If the alien is yellow, print a message that the player earned 10 points.
    # If the alien is red, print a message that the player earned 15 points.
    # Write three versions of this program, making sure each messages is printed for the appropriate  
    # alien color.

#alien_colors_3.py 

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow': 
    print("You just earned 10 points!")
else: 
    print("You just earned 15 points!")

# Exercise 4: Stages of life: ballot_box_wth_check: 

# Write an if-elif-else chain that determine a person's stage of life 

    #If a person is less than 2 years old, print a message that the person is a baby 
    #If the person is at least 2 years old, less than 4, print the message that the person is a toddler.
    #If the person is at least 4 years old but less than 13, print the message that the person is a child.
    #If the person is at least 13 years old but less than 20, print the message that the person is a teenager.
    #If the person is at least 20 years old but less than 65, print the message that the person is an adult.
    #If the person is at least 65 or older, print a message that the person is an elder.

#Python program of stages of life 

age = 18 

if age < 2: 
    print("You're a baby!")
elif age < 4: 
    print("You're a toddler!")
elif age < 13:
    print("You're a youth!")
elif age < 20:
    print("You're a young adult!")
elif age < 65: 
    print("You're an adult!")
else: 
    print("You're an elder!")

# Exercise 5: Favorite fruit ballot_box_with_check: 

# Make a list of your favorite fruits, and then write a series in independent if statements that checks certain fruits on your list. 

    # Make a list of your three favorite fruits and call it favorite_fruits.
    # Write five if statements. Each should check whether a certain kind of fruit is in your list. if the fruit is on your list, the

 #Python program: favorite fruit:

favorite_fruits = ['mango', 'banana', 'apple']

if 'mangos' in favorite_fruits:
    print("You really like mangos!")
if 'banana'in favorite_fruits: 
    print("You really like banana!")
if 'apple'in favorite_fruits:
    print("You really like apple")

