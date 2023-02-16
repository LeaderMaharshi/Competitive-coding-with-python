# Python program to insert element at a given location in Array.

def insert_element(arr, index, element):
    if index < 0 or index > len(arr):
        print("Error: Index out of range")
        return arr
    arr.insert(index, element)
    return arr

# Define an array
arr = [1, 2, 3, 4, 5]

# Insert an element (6) at index 2
new_arr = insert_element(arr, 2, 6)

# Print the new array
print(new_arr)

