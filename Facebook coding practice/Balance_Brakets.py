#Balance Brackets
#A bracket is any of the following characters: (, ), {, }, [, or ].
#We consider two brackets to be matching if the first bracket is an open-bracket, e.g., (, {, or [, and the second bracket is a close-bracket of the same type. That means ( and ), [ and ], and { and } are the only pairs of matching brackets.
#Furthermore, a sequence of brackets is said to be balanced if the following conditions are met:
#The sequence is empty, or
#The sequence is composed of two or more non-empty sequences, all of which are balanced, or
#The first and last brackets of the sequence are matching, and the portion of the sequence without the first and last elements is balanced.
#You are given a string of brackets. Your task is to determine whether each sequence of brackets is balanced. If a string is balanced, return true, otherwise, return false

#Example 2
#s = {}()
#output: true

#Example 3
#s = {(})
#output: false

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def isBalanced(s: str) -> bool:
  # Write your code here
  #creating a stack
  
  stack = []
  for c in s: #c is ')}]'
    if stack and stack[-1] == '(' and c == ')':
      stack.pop()
    elif stack and stack[-1] == '[' and c == ']':
      stack.pop()
    elif stack and stack[-1] == '{' and c == '}':
      stack.pop()
    else: 
      stack.append(c)
  
  if stack: 
    return False
  return True

print (isBalanced("{[(])}"))
print(isBalanced("{{[[(())]]}}"))