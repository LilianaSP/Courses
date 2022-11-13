#Minimizing Permutations
#In this problem, you are given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:
#Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
#Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.

#Example
#If N = 3, and P = (3, 1, 2), we can do the following operations:
#Select (1, 2) and reverse it: P = (3, 2, 1).
#Select (3, 2, 1) and reverse it: P = (1, 2, 3).
#output = 2

import math
# Add any extra import statements you may need here
from collections import deque
# Add any helper functions you may need here


def minOperations(arr):
  # Write your code here
  N = len(arr)
  target = tuple(sorted(arr))
  init_state = tuple(arr)
  q = deque ([init_state])
  visited = {init_state}
  n_levels = 0
  
  while q:
    for _ in range (len(q)):
      cur = q.popleft()

      if cur == target:
        return n_levels
      
      for i in range(N):
        for j in range(i + 1, N + 1):
          permutation = cur[:i] + cur[i:j][::-1] + cur[j:]
          
          if permutation not in visited:
            visited.add(permutation)
            q.append(permutation)
            
            
    n_levels += 1
    
  return -1


print(minOperations([1, 2, 5, 4, 3]))
print(minOperations([3, 1, 2]))