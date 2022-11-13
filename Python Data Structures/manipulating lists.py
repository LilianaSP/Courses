"""Concatenating lists using +"""
import numbers


a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

"""Lists can be sliced"""
t = [9,41,12,3,74,15]
print(t[1:3]) #up to but not including
print(t[:4])
print(t[3:])

"""Building a list from scratch"""
stuff = list() #creating an empty list
stuff.append('book')
stuff.append('99')
print(stuff)
stuff.append('cookie')
stuff.append('dogs')
print(stuff)

"""Is something in a lists?"""
print('dogs' in stuff)
print(23 in stuff)

"""Lists aare in order"""
num = [23, 4 , 5.87, 98, 32 , 76]
num.sort()
print(num) #smallest to largest
print(num[1]) #printing the position 1

"""Built-in Functions and list"""
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
operation = (sum(num)/len(num))
print(round(operation,2)) #using the function round to round the numbers to 2 decimal places

"""Excersice: Calculating an avarage between numbers"""
#way 1 without using lists -> this one uses less space in memory, is better for getting the average of a lot of numbers
total = 0
count = 0
print("\nWay 1 of making an average of numbers")
print("To get the average write done")
while True:

    inp = input("Enter a number: ")
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
average = total/count
print("Average: ", round(average,2))

#way 2 using list -> this one uses more space in memory, becasue it almacenates the whole numbers of the list
print("\nWay 2 of making an average of numbers")
print("To get the average write done")
numlist = list() #create empty list
while True:
    inp = input("Enter a number: ")
    if inp == "done": break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print("Average: ", round(average,2))


