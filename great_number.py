
def great_number(*args):
    numbers = list(args)
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    print(max_num)



great_number(2,3,4,5)