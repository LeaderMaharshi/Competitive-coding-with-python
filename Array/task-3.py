#Write a program in Python for,
# How to find all pairs in array of integers whose sum is equal to given number.



# array of integers
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

target = 26

pairs = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        # check if sum of pair is equal to given number
        if arr[i] + arr[j] == target:
            # add pair to list
            pairs.append((arr[i], arr[j]))

for pair in pairs:
    print(pair)