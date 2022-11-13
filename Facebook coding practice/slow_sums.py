#Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number: Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each operation equal to the value of the new number, and call the penalty for the entire list as the sum of the penalties of each operation.
#For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, which would transform the list into [1, 5, 4, 5] and incur a penalty of 5. The goal in this problem is to find the highest possible penalty for a given input.

#Example
#arr = [4, 2, 1, 3]
#output = 26
#First, add 4 + 3 for a penalty of 7. Now the array is [7, 2, 1]
#Add 7 + 2 for a penalty of 9. Now the array is [9, 1]
#Add 9 + 1 for a penalty of 10. The penalties sum to 26.

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getTotalTime(arr):
  # Write your code here
  #you pick the largets integers and make the sum 
  
  arr.sort(key = lambda x: -x) #to sort the list
  #[4, 3, 2, 1]
  
  for i in range(1, len(arr)):
    arr[i] += arr[i-1]
    
  return sum(arr[1:])
  
print (getTotalTime([2, 3, 9, 8, 4]))