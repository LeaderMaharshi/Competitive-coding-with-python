# Python Program to delete given element from Array.

def delete_element(arr, element):

    if element not in arr:
        print("Error: The element is not found in arry")
        return arr
    arr.remove(element)
    return arr

# Define an array
arr = [1, 2, 3, 4, 5]

# Delete the element 3 from the array
new_arr = delete_element(arr, 3)

# Print the new array
print(new_arr)

