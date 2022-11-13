#Median Stream
#You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the median of the elements arr[0..i] (rounded down to the nearest integer).
#The median of a list of integers is defined as follows. If the integers were to be sorted, then:
#If there are an odd number of integers, then the median is equal to the middle integer in the sorted order.
#Otherwise, if there are an even number of integers, then the median is equal to the average of the two middle-most integers in the sorted order.

#Example 1
#n = 4
#arr = [5, 15, 1, 3]
#output = [5, 10, 5, 4]
#The median of [5] is 5, the median of [5, 15] is (5 + 15) / 2 = 10, the median of [5, 15, 1] is 5, and the median of [5, 15, 1, 3] is (3 + 5) / 2 = 4.

import math
# Add any extra import statements you may need here
import heapq

# Add any helper functions you may need here


def findMedian(arr):
  # Write your code here
  
  smal_half = []
  large_half = []
  ret = []
  
  for i, x in enumerate(arr):
    
    if i%2 == 0:
      heapq.heappush(smal_half, -heapq.heappushpop(large_half,x))
      ret.append(-smal_half[0])
    else:
      heapq.heappush(large_half, -heapq.heappushpop(smal_half, -x))
      ret.append((large_half[0] -smal_half[0])//2)
      
  return ret