
def find_average(*args):
    print(len(args))
    if len(args) == 0:
        return None
    else:
        total_sum = sum(args)
        total_length = len(args)
        average = total_sum / total_length
        return average

print(find_average(5,6,7,8,9,5))