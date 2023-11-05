# Chapter 5 Exercises 

# Exercise 1: person ballot_box_with_check:

# Use a dictionary to store the information about a person you know. Store their first name, age, the city, in which they live. 
# You should have keys such as first_name, last_name, and city. Print each piece of information stored in your library. 

#person.py

person = {
    'first_name': 'linda',
    'last_name': 'llouw',
    'age': 37,
    'city': 'cape town',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# Exercise 2: glossary ballot_box_with_check: 

# A python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it glossary. 

    # Think of five programming words you've learned about the previous chapters. Use these words as the keys in glossary and store their meaning of their values.
    # Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then the meaning, or print.

 # The word in one line and then print its meaning intended on a second line. Use the newline character (\n) to insert blank line in between. 

#each word-meaning pair in your output. 

#glossary.py 

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")


# Exercise 3: Glossary 2 ballot_box_wth_a_check

# Now that you how to loop through a dictionary, clean up the code from exercise 6-3 (page 99) by replacing your series of print().
# Calls with a loop and runs through the dictionary's keys and values. Where you're sure that your loop works and add five more python terms.
# To your glossary. When you run your program again, these words and meaning should automatically be included in the output. 

#glossary_2.py 

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")

# Exercise 4: Rivers ballot_box_with_check: 

# Make a dictionary containing three major rivers and the country each rivers run through. One key-value pair might be 'nile': egypt. 

    # Use a loop to print a sentence about each river, such as the Nile runs through Egypt.
    # Use a loop to print the name of each river included in the dictionary.
    # Use a loop to print the name of each country included in the dictionary. 

#rivers.py 

rivers = {
    'nile': 'egypt',
    'anderson' : 'canada',
    'moskva': 'Russia',
    'pearl': 'mexico',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries are included in this data set:")
for river in rivers.keys(): 
     print(f"- {river.title()}")

# Exercise 5: pets ballot_box_with_check: 

# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner's name.
# Store these dictionaries in a list called pets. Next loop through your list as you do print everything you know about each pet.

#pets.py 
# Make an empty list to store pets in.

pets = []

# Make individual pets, and store each one in the list.

pet = {
    'animal type': 'cats',
    'name': 'Snow', 
    'owner': 'katty',
    'weight': 2,
    'eats': 'tuna'
}

pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'Oreo', 
    'Owner': 'Daniel',
    'Weight': 3,
    'eats': 'chicken',
}
 
pets.append(pet)

# Display information about each pet 

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

