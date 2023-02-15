
string = "Hello world"

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string

str = remove_vowels(string)
print(str)