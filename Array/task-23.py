# Python Program to find highest frequency element in array.

from collections import Counter

def highest_frequency(arr):
    frequency = Counter(arr)
    highest_freq_element = max(frequency, key=frequency.get)
    return highest_freq_element

# Define an array
arr = [1, 2, 3, 2, 1, 2, 3, 3, 3]

# Find the element with the highest frequency in the array
highest_freq_element = highest_frequency(arr)

# Print the element with the highest frequency
print(highest_freq_element)
