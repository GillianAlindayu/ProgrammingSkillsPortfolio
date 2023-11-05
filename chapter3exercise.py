# Chapter 3 Data structures 

#Exercise 1 : Names ballot_box_wth_check 
#Store the names of few of your friends in a list. Print each names by accessing each element in the list, one at the time.

names = ['Lai', 'Sam', 'Jam']

print(names[0])
print(names[1])
print(names[2])


# Exercise 2: Greetings ballot_box_with_check: 

#start with the list you used in exercise 1, but instead you just printing each person's name text of each message should be personalized with the name 

names = ['lai', 'sam', 'Jam']

msg = "hello, " + names[0].title() + "!"
print(msg)

msg = "hello, " + names[1].title() + "!"
print(msg)

msg = "hello, " + names[2].title() + "!"
print(msg)

# Exercise 3: your own list ballot_box_with_check 


#think of your favorite mode of transportation such as motorcycle or car and make a list that stores a several examples. Use your list
#to print a series of your statements about these items, such as "I would like to own a honda motorcycle."

#favorite motorcycle 

#print the names of all motorcycles 

motorcycles = ['Honda', 'Yamaha', 'Suzuki']

for motorcycle in motorcycles: 
    print(motorcycle)

print("\n")

#print the sentence about each motorcycle 

for motorcycle in motorcycles: 
    print(f"I really love {motorcycle} motorcycles!")

print("\n I really love motorcycle!")

# Exercise 4: Guest list ballot_box_with_check: 

# If you could invite anyone living or deceased, to a dinner who would you invite? 
# Make a list that can includes at least three people you'd invite for dinner 

# print a message for you to invite them for dinner: 

guest_for_dinner = ['Daniel', 'April', 'Faith']

names = guest_for_dinner[0].title()
print(f"{names}, please come to dinner.")

names = guest_for_dinner[1].title()
print(f"{names}, please come to dinner.")

names = guest_for_dinner[2].title()
print(f"{names}, please come to dinner. ")

# Exercise 5: Changing guest list ballot_box_with_check: 

# You just heard that one of your guest can't make it to dinner, so you need to send out a new set of invitations 
# You will have to think of someone else to invite.

# Start a program with 3-4, add a print() call the end of the program and stating the name of the guest who can't make it 
# Modify your list, replacing the name of the guest who can't make it with the same name of the new person that you're inviting. 
# Print a second set of invitation messages, one for each person who is still on your list. 

#Invite some people to dinner 

guest_for_dinner = ['Daniel', 'April', 'Faith']

names = guest_for_dinner[0].title()
print(f"{names}, please come to dinner.")

names = guest_for_dinner[1].title()
print(f"{names}, please come to dinner.")

names = guest_for_dinner[2].title()
print(f"{names}, please come to dinner.")

names = guest_for_dinner[0].title()
print(f"\nSorry,{names}, I can't make it to dinner.")

# Daniel can't make it to dinner.

del(guest_for_dinner[0])
guest_for_dinner.insert(0, 'Analyn')

# print invitations again 

names = guest_for_dinner[0].title()
print(f"\n{names}, please come to dinner.") 

names = guest_for_dinner[1].title()
print(f"{names}, please come to dinner.")

names = guest_for_dinner[2].title()
print(f"{names}, please come to dinner.")

# Exercise 6: Shrinking Guest list ballot_box_with_check:

# Start your program from exercise 3-5. Add a new line that prints a message that you can invite two people for dinner 

#invite some people to dinner 

# Invite some people to dinner.
guests = ['Daniel', 'April', 'Faith']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Jack can't make it! Let's invite Gary instead.
del(guests[1])
guests.insert(1, 'Analyn')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'Peter')
guests.insert(2, 'Rover')
guests.append('George')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])


# Exercise 7: seeing the world ballot_box_with_check:

#Think of at least five places in the world that you'd visit. 
    # store the locations in a list. Make sure the list is not in alphabetical order.
    # Print Your list in an original order by printing it.
    # Use your sorted () to print your list in reverse alphabetical order without changing the order of the original list.
    # Show that your list is still in original order by printing it again.
    # Use reverse() to print your list in reverse alphabetical order without changing the order of the original list 
    # Use reverse() to change order of your list again. Print the list to show back to its original order. 
    # Use sort() to change your list so it's stored in alphabetical order. Print the list that its order has been changed.
    # Use sort() to change your list so it's stored to reverse alphabetical order. Print the list to show that its ordered has change 


locations = [ 'Seoul', 'Tokyo', 'London', 'Stockholm', 'Bern' ]

print("Original order: ")
print(locations)

print("\nAlphabet order: ")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)


