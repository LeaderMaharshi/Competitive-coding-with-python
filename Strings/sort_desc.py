def sort_string(string):
    """Sorts the characters of a string in ascending order and returns the sorted string."""
    sorted_string = ''.join(sorted(string, reverse=True))
    return sorted_string

string = "hello world"
sorted_string = sort_string(string)
print(sorted_string)