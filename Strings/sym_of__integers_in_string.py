def sum_of_integers_in_string(string):
    """Calculates the sum of integers in a string."""
    nums = []
    current_num = ""
    for char in string:
        if char.isdigit():
            current_num += char
        else:
            if current_num:
                nums.append(int(current_num))
                current_num = ""
    if current_num:
        nums.append(int(current_num))
    return sum(nums)


string = "hfh78afba3248hj"

print(sum_of_integers_in_string(string))