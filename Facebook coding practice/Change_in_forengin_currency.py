#You likely know that different currencies have coins and bills of different denominations. In some currencies, it's actually impossible to receive change for a given amount of money. For example, Canada has given up the 1-cent penny. If you're owed 94 cents in Canada, a shopkeeper will graciously supply you with 95 cents instead since there exists a 5-cent coin.
#Given a list of the available denominations, determine if it's possible to receive exact change for an amount of money targetMoney. Both the denominations and target amount will be given in generic units of that currency.

#Example 1
#denominations = [5, 10, 25, 100, 200]
#targetMoney = 94
#output = false
#Every denomination is a multiple of 5, so you can't receive exactly 94 units of money in this currency.

#Example 2
#denominations = [4, 17, 29]
#targetMoney = 75
#output = true
#You can make 75 units with the denominations [17, 29, 29].

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def canGetExactChange(targetMoney: int, denominations: list) -> bool:
  # Write your code here
  if targetMoney == 0:
    return True
  
  if targetMoney < 0:
    return False
  for d in denominations:
    if canGetExactChange(targetMoney - d, denominations):
      return True
  return False
  
print(canGetExactChange(75,[4, 17, 29]))
print(canGetExactChange(94,[5, 10, 25, 100, 200]))