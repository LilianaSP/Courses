#Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
#If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.

#Example 1
#n = 5
#k = 6
#arr = [1, 2, 3, 4, 3]
#output = 2
#The valid pairs are 2+4 and 3+3.

import math
# Add any extra import statements you may need here
from collections import Counter

# Add any helper functions you may need here


def numberOfWays(arr, k):
   # Write your code here
    
    d = Counter(arr)  #dictionary
    num_times = 0
      
    for key in d:
      if k - key in d:
        if k - key == key:
          val = d[key]
          num_times += val*(val-1)/2
        else:
          num_times += d[key] * d[k -key]/2
          
      
      
      
    return num_times
  
print(numberOfWays([1, 5, 3, 3, 3], 6))