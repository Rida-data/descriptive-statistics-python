
# Descriptive Statistics with Python
# My first statistics project

from statistics import mode, median

numbers = [10, 20, 20, 30, 40]

# Calculate descriptive statistics
average = sum(numbers) / len(numbers)
from statistics import median
middle = median(numbers)
most_common = mode(numbers)
data_range = max(numbers) - min(numbers)

# Display the results
print("Numbers:", numbers)
print("Mean:", average)
print("Median:", middle)
print("Mode:", most_common)
print("Range:", data_range)
