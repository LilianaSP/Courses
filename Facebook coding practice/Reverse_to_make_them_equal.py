import math
# Add any extra import statements you may need here

from collections import Counter
#Counter allow us to know the times that a number apear in an array
# Add any helper functions you may need here


def are_they_equal(array_a, array_b):
  # Write your code here
  return Counter(array_a) == Counter(array_b)
  
  
print (are_they_equal([1, 2, 3, 4],[1, 4, 3, 2] ))