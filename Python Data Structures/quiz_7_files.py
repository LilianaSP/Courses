"""7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at"""

# Use words.txt as the file name
# use the file name as an input
fname = input("Enter file name: ") #we ask the user to write the name of the file
fh = open(fname, 'r') #we open the file

for i in fh.readlines(): #use the function readlines() to read the file
    print(i.upper().rstrip()) #upper() to make every letter uppercase, then rstrip to eliminate the newline between each line