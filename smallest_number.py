
def smallest_number(*args):
    numbers = list(args)
    smallest_number = numbers[0]
    for i in numbers:
        if i < smallest_number:
            smallest_number = i
    print(smallest_number)

smallest_number(1,2,3,4,5,6,7)