import math
# Add any extra import statements you may need here
from collections import deque

# Add any helper functions you may need here


def findPositions(arr: list, x: int) -> list:
  # Write your code here
  
  deq = deque() #we initialice the variable
  for e in enumerate(arr):
    deq.append(e)
  out = []
  for _ in range(x):
    #firts we initializate the variables 
    maximum = float('-inf')
    i = 0
    pop_list = []
    ind_to_remove = None
    while deq and i < x:
      popped = deq.popleft() #setp number 1 pop the elemets of x
      if popped[1] > maximum: #to found the maximum
        maximum = popped[1]
        ind_to_remove = popped[0]
      pop_list.append(popped)
      
      i += 1
    for t in pop_list:
      if t[0] != ind_to_remove:
        deq.append( (t[0], max(0, t[1]-1)))
        
    out.append(ind_to_remove + 1)
    
    
  return out

print (findPositions([1, 2, 2, 3, 4, 5], 5))