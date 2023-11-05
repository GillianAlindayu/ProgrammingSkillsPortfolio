# Chapter 7 Functions: exercises.

# Exercise 1: message: ballot_box_with_check

# Write a function called display_message that prints one sentence telling everyone that you are learning about in this chapter.
# Call the function, and make sure the message displays correctly. 

# Python program of message 

def display_message():
    """Display message about what I am learning."""
    msg = "I am learning to store code about functions."
    print(msg)

display_message()

# Exercise 2: Favorite book: ballot_box_with_check: 

# Write a function called favorite_book() that accepts one parameter, title.
# The function should ptint a message, such as one of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

# python program of favorite book 

def favorite_book(title):
    """Display the message about someone's favorite book."""
    print(f"{title} is one of my favorite books.")

favorite_book("Alice in Wonderland")

# Exercise 4: T-shirt ballot_box_with_check: 

# Write a function called make_chirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
 
def make_shirt(size, message): 
    """Summarize the shirt that's going to be made."""
    print(f"I am going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt('short', 'I love Python!')
make_shirt(message= "You're cool.", size= "short")

# Large shirts 

# Modify the make_shirt() so that shirts are large by default with a message that needs I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# Python program of large shirts 

def make_shirt(size= 'large', message= 'I love Python!'): 
    """Summarize the shirt that's going to be made."""
    print(f"\nI'am going to make a {size} t-shirt.")
    print(f'It will say, "{message}" ')

make_shirt()
make_shirt(size= 'medium')
make_shirt('small', 'Programmers are code blooded.')

# Exercise 4: cities: ballot_box_with_check: 

# Write a function called describe_city() that accepts and its country.
# The function should print a simple sentence, such as  Reykjavik is in Iceland. Give the parameter for the country a default value.

# Python program names of the city

def city_country(city, country):
    """Return a string like 'Reykjavik, Iceland'. """
    return f"{city.title()}, {country.title()}"

city = city_country('Reykjavik', 'iceland')
print(city)

city = city_country('Oslo', 'Norway')
print(city)

city = city_country('Copenhagen', 'Denmark')
print(city)




  