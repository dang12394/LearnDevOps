import random

# Generate 6 unique random numbers between 1 and 55
random_numbers = random.sample(range(1, 56), 6)

# Sort the numbers in ascending order
random_numbers.sort()

# Print the sorted numbers
print(random_numbers)