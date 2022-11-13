#Encrypted messages
#Rotational factor
import math
import string
#Example 1
plain_text = 'hello world!'
shift = 7 #we determine our rotational factor

alphabet = string.ascii_lowercase #we create our alphabet, the one that is going to rotate 
shifted = alphabet[shift:] + alphabet[:shift]#ewe start form de shifted letter and then we append the rest of the alphabet to that string

#we need to create a interpreter table
table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)
print(encrypted)

#Example 2
plain_text_2 = 'zebra?' #here we write the text that we want to encrypted
shift = 3 #we determine the rotational shift 

alphabet = string.ascii_lowercase #we create our alphabet string
shifted2 = alphabet[shift:] + alphabet[:shift] 

table = str.maketrans(alphabet, shifted2)
encrypted2 = plain_text_2.translate(table)
print (encrypted2)
print('\nNote: in both examples we are only using strings and lowercase letterts')

print('\nExample 3: creating our alphabet to work with any kind of character: ')

def ceasar(text, shift, alphabets):
  def shift_alphabet(alphabet):
    return alphabet[shift:] + alphabet[:shift]

  shifted_alphabets = tuple(map(shift_alphabet, alphabets))
  final_alphabet = ''.join(alphabets)
  final_shifted_alphabet = ''.join(shifted_alphabets)
  table = str.maketrans(final_alphabet, final_shifted_alphabet)
  return text.translate(table)


plain_text_3 = 'This is a string342. Hello World!'
#We call the function that we created with the shifted shifted_alphabets
print(ceasar(plain_text_3,7,[string.ascii_lowercase, string.ascii_uppercase, string.punctuation])) 
#note: if we do not want to change the punctuation symbols, we only remove the string.punctuation at the moment of calling the function


  