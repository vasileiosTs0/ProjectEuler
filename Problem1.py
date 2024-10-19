# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6, and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import math

max_number = 1000 # Define end number
multipliers = [3,5] # Define multipliers

list_of_multipliers = [] # Create an empty list
for number in multipliers:
    multiplier = int(math.floor((max_number)/number)) # Find how many times the number fits in the max number 
    if (max_number % number) != 0:
        multiplier = multiplier + 1 
        
    list_of_multipliers.extend([i*number for i in range(1, multiplier)]) # Append the list 
   
list_of_multipliers = list(set(list_of_multipliers)) # Remove duplicates

print("Solution: ", sum(list_of_multipliers))  
