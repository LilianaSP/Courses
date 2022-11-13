import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

arr_1 = [(7, 6, 5), (5, 7, 6), (8, 2, 9), (2, 3, 4), (2, 4, 3)]

#writing code in one line 
#def countDistinctTriangles(arr: list) -> int:
  #return len(set(map(lambda t : tuple(sorted(t)), arr)))
def countDistinctTriangles(arr: list) -> int:
  triangle = set()
  for t in arr: 
    triangle.add(tuple(sorted(t))) #sorted of a tuple gives you a list, it does not matter if there are repitead numbers 
  return len(triangle)

print(countDistinctTriangles([(7, 6, 5), (5, 7, 6), (8, 2, 9), (2, 3, 4), (2, 4, 3)]))