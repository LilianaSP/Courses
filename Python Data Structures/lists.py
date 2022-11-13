"""Collections using lists"""

#list constants
print([1,24,76])
print(["red", "yellow","blue"])
print(["red", 24, 98.6])
#list can be empty
print([])
#three element list, list into list
print([1,[5,6],7])

"""Lists and Definite Loops"""
friends = ["Joseph", "Sally", "Glenn"]
for friend in friends: #friend is just the name of the variable
    print("Happy new year: ", friend) #write the print statement in the for loop to print the name of each friend 
    #until finish with the list
print("Done")

"""Looking inside lists"""
print(friends[1])

"""List are mutable"""
fruit = "Banana"
x = fruit.lower()
print(x)

#we can't do this
#fruit[0]= 'b' because we are dealing with strings not with lists
#example 2

lotto = [2,14,26,41,63]
print(lotto)
#modifiying list
lotto[2]= 28 # position 2 of the list lotto change to 28
print(lotto)
#lenght of the list
print(len(lotto))

"""Using the range function
-> it returns a list"""
print(range(4))
print(len(friends))
print(range(len(friends)))

#using the function of range in a for loop 
for i in range(len(friends)):
    friend = friends[i] # index operator
    print("Happy new year: ", friend)