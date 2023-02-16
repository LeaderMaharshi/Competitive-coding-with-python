# Write a program in Python to remove duplicate elements form array.

arr = [1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 9, 10]

new_arr = []

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print(new_arr)