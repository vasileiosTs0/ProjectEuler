# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number 600851475143?

def find_largest_prime(n):
prime = 2 # Initialise with the smallest prime number
  
# Keep dividing until the number is no longer dividable
while prime * prime <= n:
if n % prime:
prime += 1
else:
n //= prime
print(f"Current factor: {prime} - Remaining: {n}")

return n


number = 600851475143

# Call the function and print the result
largest_prime = find_largest_prime(number)
print(f"Solution: The largest prime factor for {number} is {largest_prime}.")     
