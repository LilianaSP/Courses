
import numpy as np
from os import system
system("clear")
def solution(numbers):
    #numbers = [65, 68, 72, 59, 72]
    maxElement = np.amax(numbers)
    minElement = np.amin(numbers)
    operation = (maxElement/minElement)*100 -100
    return operation 

numbers = [65, 68, 72, 59, 72]
print (solution(numbers))