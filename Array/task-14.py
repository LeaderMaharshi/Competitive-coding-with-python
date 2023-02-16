# Python Program to delete element at end of Array.

def delete_last_element(arr):
    if len(arr) == 0:
        print("Error: array is empty")
        return arr
    arr.pop()
    return arr

# Define an array
arr = [1, 2, 3, 4, 5]

# Delete the last element of the array
new_arr = delete_last_element(arr)

# Print the new array
print(new_arr)
