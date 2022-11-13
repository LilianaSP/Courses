#1 Billion Users
#We have N different apps with different user growth rates. At a given time t, measured in days, the number of users using an app is g^t (for simplicity we'll allow fractional users), where g is the growth rate for that app. These apps will all be launched at the same time and no user ever uses more than one of the apps. We want to know how many total users there are when you add together the number of users from each app.
#After how many full days will we have 1 billion total users across the N apps?

#Example 1
#growthRates = [1.5]
#output = 52

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getBillionUsersDay(growth_rates):
  # Write your code here
  
  start = math.ceil(math.log10((10**9) / len(growth_rates)) / math.log10(max(growth_rates)))
  end = math.ceil(math.log10((10**9) / len(growth_rates)) / math.log10(min(growth_rates)))
  Bil = 10**9
  
  while start < end:
    mid = (start + end)// 2
    gr_1 = sum ([i ** mid for i in growth_rates])
    gr_2 = sum([i ** (mid +1) for i in growth_rates])
    if gr_1 < Bil and gr_2 > Bil:
      return mid + 1
    elif gr_1 < Bil:
      start = mid
    else:
      end = mid -1
      
      