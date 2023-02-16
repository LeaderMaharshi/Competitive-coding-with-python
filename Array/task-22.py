# Python Program to merge two arrays.

def merge_arrays(arr1, arr2):
    # Concatenate the two arrays
    merged_arr = arr1 + arr2

    return merged_arr

# Define two arrays
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

# Merge the two arrays
merged_arr = merge_arrays(arr1, arr2)

# Print the merged array
print(merged_arr)
