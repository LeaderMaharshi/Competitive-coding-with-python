
string = "hello world"

def highest_frequency(string):
    char_string = {}
    for char in string:
        if char in char_string:
            char_string[char] += 1
        else:
            char_string[char] = 1
    max_count = max(char_string.values())
    return [char for char, count in char_string.items() if count == max_count]

result = highest_frequency(string)
print(f"The highest frequency character(s) in the string is/are: {', '.join(result)}")