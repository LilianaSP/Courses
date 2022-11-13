import math
# Add any extra import statements you may need here
import heapq

# Add any helper functions you may need here
#Largest Triple Products
#You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the product of the three largest elements out of arr[0..i] (or equal to -1 if i < 2, as arr[0..i] then includes fewer than three elements).
#Note that the three largest elements used to form any product may have the same values as one another, but they must be at different indices in arr.

#Example
#n = 5
#arr = [1, 2, 3, 4, 5]
#output = [-1, -1, 6, 24, 60]
#The 3rd element of output is 3*2*1 = 6, the 4th is 4*3*2 = 24, and the 5th is 5*4*3 = 60.

def findMaxProduct(arr):
  # Write your code here
  
  
  out= []
  h = [] #creating a heap
  for e in arr:
    heapq.heappush(h, e)
    if len(h) < 3:
      out.append(-1)
    else:
      if len(h) > 3:
        heapq.heappop(h)
      out.append(h[0]*h[1]*h[2])
      
      
  return out
          
print (findMaxProduct([4, 4, 8, 13, 6]))