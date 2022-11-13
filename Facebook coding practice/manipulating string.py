import os
os.system('clear')

"""Manipulating strings"""
#concatenation
a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)

#using in
fruit = 'banana'
'n' in fruit
#True
'm' in fruit
#False

if 'a' in fruit:
    print('Found it')

"""String Libary"""
greet = 'Hello Bob'
zap = greet.lower() #creating a string in lower cases
print(zap)
print(greet)
zep = greet.upper() #creating a string in upper cases
print(zep)

"""Get the position of string elements using .find"""
pos = fruit.find('na')
print(pos)

"""Search and replace"""
nsrt = greet.replace('Bob', 'Jane')# we use the replace function to change strings
print(nsrt)

nstr = greet.replace('o','x')
print(nstr)

"""Prefixes"""
line = 'Please have a nice day'
line.startswith('Please')
#True
line.startswith('p')
#False

"""Parsing and extracting"""
data = 'from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2002'
atpos = data.find('@') #search the @
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)