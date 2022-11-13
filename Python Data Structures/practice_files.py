"""Practice with files, we are using the file_processing.txt file"""
#write a function to read an entire text file
def ReadFile(fname):
    txt = open(fname)
    print(txt.read())


print("++++Reading a whole file and printing it on the terminal++++")
print("\n")
ReadFile("file_processing.txt")
print("\n")

def Nlines(fname):
    count = 0
    txt = open(fname)
    for line in txt:
        count = count +1
    print("Line count: ", count) #the print statement goes out of the for loop, otherwise, it will print the same 
    #statement the number of lines of the text file

print("++++Counting the lines of the file and printing them++++") 
Nlines("file_processing.txt")
print("\n")


    