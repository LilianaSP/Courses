
from os import system
system("clear")
"""Working with files"""
#first we have to open the file that we are going to work on
xfile = open("file_processing.txt") #we use the function open("name of the file")
"""We create a for loop to print the entire file"""
for cheese in xfile: 
    print(cheese)

"""Counting lines in a file"""
#we initialize the counter
xfile = open("file_processing.txt")
count = 0
for line in xfile:
    count = count + 1 # the counter will count the next line in the file
print("Line count: ", count)

"""Reading the whole file"""
xfile = open("file_processing.txt")
red_file = xfile.read()
print(len(red_file)) # gives you the total characters of the file
print(red_file[:10]) #prints the firts 10 characters ofthe file (spaces included)

"""Searching through a file"""

xfile = open("file_processing.txt")
for line in xfile:
    if line.startswith('From: '): #search the word from:, and prints the whole line
        print(line)

"""Searching through a file (*fixed, without the spaces between lines)"""
xfile = open("file_processing.txt")
for line in xfile:
    line = line.rstrip() #we use rstrip() to delete the newline between each line
    if line.startswith("From: "):
        print(line)

"""Skipping with continue"""
xfile = open("file_processing.txt")
for line in xfile:
    line = line.rsplit()
    if not "@uct.ac.za" in line:
        continue
    print(line)