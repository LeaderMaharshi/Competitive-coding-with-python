string = "Hello world"

def remove_str(string):
    new_string = ""
    for char in string:
        if char not in new_string:
            new_string += char
    return new_string

print(remove_str(string))
