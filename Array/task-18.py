# print even numbers

def print_even(arr):
    even=[]
    if len(arr) == 0:
        print("Error: no elements found")
    else:
        for i in arr:
            if i % 2 == 0:
                even.append(i)
    return even
arr = [1, 2, 3, 4, 5]
result = print_even(arr)
print(result)
