# Declare variable
sum = 0

# Find the sum of all multiples of 3 and 5 below 1000
for x in range(1,1000):
    if (x%3 == 0 or x%5 == 0):
        sum += x

# Print the sum
print(sum)
