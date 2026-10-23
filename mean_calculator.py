
# Descriptive Statistics with Python
# My first statistics project

from statistics import mode

numbers = [10, 20, 20, 30, 40]

# Calculate descriptive statistics
average = sum(numbers) / len(numbers)
middle = sorted(numbers)[len(numbers) // 2]
most_common = mode(numbers)

# Display the results
print("Numbers:", numbers)
print("Mean:", average)
print("Median:", middle)
print("Mode:", most_common)
