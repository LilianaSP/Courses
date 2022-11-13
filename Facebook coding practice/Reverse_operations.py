#Reverse Operations
#You are given a singly-linked list that contains N integers. A subpart of the list is a contiguous set of even elements, bordered either by either end of the list or an odd element. For example, if the list is [1, 2, 8, 9, 12, 16], the subparts of the list are [2, 8] and [12, 16].
#Then, for each subpart, the order of the elements is reversed. In the example, this would result in the new list, [1, 8, 2, 9, 16, 12].
#The goal of this question is: given a resulting list, determine the original order of the elements.

#Example
#Input:
#N = 6
#list = [1, 2, 8, 9, 12, 16]
#Output:
#[1, 8, 2, 9, 16, 12]

import math
# Add any extra import statements you may need here


class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

# Add any helper functions you may need here


def reverse(head):
  # Write your code here
  node = head
  output = []
  
  while node:
    is_even = node.data % 2 == 0
    if is_even :
      output.append(node) 
      
    if not is_even or node.next is None: #when it is not even it starts popping
      left, right = 0, len(output)-1
      while len(output) > 1 and left < right:
      
        output[left].data, output[right].data = output[right].data,  output[left].data #swaping node data
        left += 1
        right -= 1
        
      output.clear()
    node = node.next
  return head
