from os import system
system("clear")
print("Excersise 6.5")

str = "X-DSPAM-Confidence: 0.8475"
print(str)

ipos = str.find(":") #we find the position where the : is
print (ipos) # we print that position
piece = str[ipos+2:] # we add piece +1 because we want to print only the numbers
#print(piece) output (: 0.8475)
print(piece) #output 0.8475


value = float(piece) #converting string to float
print(value)

#using value as a float number
print(value + 45.6)

abc = "With three words"
stuff = abc.split() #we use the split() function to split the string into a list
print(stuff) #output ['With', 'three', 'words']
print(stuff[0]) #output With

for w in stuff:
    print(w)