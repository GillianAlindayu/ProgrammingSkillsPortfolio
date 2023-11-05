#Chapter 2 EXERCISES 

# Exercise 1: Variables: ballot_box_with_check: 
#Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message 

#Python program to Assign a message to a variable 

msg = "hello, this is Gillian"
print(msg)

#Another method of simple message 
msg = "You won the game!!"
print(msg)

msg = "You completed your first level!!"
print(msg)

# Exercise 2 : Variables ballot_box_with_check:
# Find a quote from a famous person you admire print the quote and the name and its author 

#Your output should look something like the following including the quotation marks: 

print('Donnie Yen once said, "I would like to choose projects, ')
print('that will allow me as an artist to make my art." ')

# Exercise 3: stripping name ballot_box_with_check:

# Use the variable to represent a person's name and include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, \t" and \n", at least once. 

#print the name once, so the whitespace around the name is displayed.
#Then print the name using each of the three stripping functions: lstrp(), rstrip(), and strip().

#Python code using stripping 
#string 

a = "\tGillian Alindayu\n"
print(a)
print(a.lstrip())
print(a.rstrip())
print(a.strip())

#in other solution of stripping names:
name = '\tGillian Alindayu\n'
print(name)

print("undefined: ")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrp():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())

# Exercise 4: Favorite number ballot_box_with_check:

#Use a variable to represent your favorite number: Then using that variable, create a message that reveals your favorite numbaer  
#print that message 

fave_num = 30 
msg = "my favorite number is " + str(fave_num) + "."
print(msg)

# Exercise 5: USB shopper ballot_box_with_check
#Write a program that calculates how many USB that she can have and how many pounds she will have left.

#You will use the arithmetic operators to complete the exercise 

USB_sticks_brought = ("total USB Sticks brought are = ")
money_left = "total money that is left= "
print(USB_sticks_brought + str(int(50/6)))






