# Python Program to delete element from array at given index.

def remove_element_index(arr,  index):
    if index < 0 or index > len(arr):
        print("Error: Out of range")
        return arr
    del arr[index]

    return arr

# Define an array
arr = [1, 2, 3, 4, 5]

# Delete the element at index 2 from the array
new_arr = remove_element_index(arr, 2)

# Print the new array
print(new_arr)

