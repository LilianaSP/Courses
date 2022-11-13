import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def balancedSplitExists(arr: list) -> bool:
  # Write your code here
  #example array  [1, 5, 7, 1]
  #array sorted into A = [1, 1, 5] and B = [7].
  arr.sort()
  #example array  [1,, 1, 5, 7]
  arr_cumsum = arr.copy()
  for i in range(1, len(arr_cumsum)):
    arr_cumsum[i] += arr_cumsum[i-1]
    # [1, 2, 7, 14]
  for i in range(len(arr)-1):
    if arr_cumsum[i] * 2 == arr_cumsum[-1] and arr[i] != arr[i+1] :
      return True
  return False

print(balancedSplitExists([2, 1, 2, 5]))
  # expected True 
print(balancedSplitExists([3, 6, 3, 4, 4]))
#expected False