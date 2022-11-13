#Magical Candy Bags
#You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
#It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), and as soon as you finish, the bag mysteriously refills. If there were x pieces of candy in the bag at the beginning of the minute, then after you've finished you'll find that floor(x/2) pieces are now inside.
#You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?

#Example 
#N = 5 
#k = 3
#arr = [2, 1, 7, 4, 2]
#output = 14
#In the first minute you can eat 7 pieces of candy. That bag will refill with floor(7/2) = 3 pieces.
#In the second minute you can eat 4 pieces of candy from another bag. That bag will refill with floor(4/2) = 2 pieces.
#In the third minute you can eat the 3 pieces of candy that have appeared in the first bag that you ate.
#In total you can eat 7 + 4 + 3 = 14 pieces of candy.

import math
# Add any extra import statements you may need here

import heapq
# Add any helper functions you may need here


def maxCandies(arr: list, k:int) -> int:
  # Write your code here
  
  arr = [-x for x in arr]
  heapq.heapify(arr) #creates a min heap, so we change thye sign of the array. Now our min heap is our max heap
  
  num_candy = 0
  
  for _ in range(k):
    pop = -heapq.heappop(arr) #to undo the - sign effect, we have to put another - sign in front of the heapq
    num_candy += pop
    heapq.heappush(arr, -(pop//2))
  
  return num_candy

print(maxCandies([19, 78, 76, 72, 48, 8, 24, 74, 29], 9))