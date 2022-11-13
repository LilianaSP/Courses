import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(s, rotation_factor):
  out = ''
  for c in s:
    if c.isnumeric():
      out += str((int(c) + rotation_factor) % 10)
    elif c.isupper():
      t = (ord(c) - ord('A')+rotation_factor) % 26
      out += chr(ord('A') + t)
    elif c.islower():
      t = (ord(c)-ord('a') + rotation_factor) % 26
      out += chr(ord('a') + t)
    else:
      out += c
      
  return out

print (rotationalCipher('Hello435', 3))