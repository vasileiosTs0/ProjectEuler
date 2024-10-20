# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with  and , the first terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.


fib_table = [1, 2] # Initialise fibonacci sequence
latest_value = table[-1]
limit = 4000000

while latest_value < limit:
    latest_value = sum(fib_table[-2:]) # Calculate the latest fibonacci number
    if latest_value > limit:
        break
    fib_table.append(latest_value) # Append the table 

print("Solution: ", sum(num for num in fib_table if not num%2)) # Print result
