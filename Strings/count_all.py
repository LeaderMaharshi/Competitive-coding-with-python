
def count_char(string):
    alphabets = digits = specials = 0
    string = string.replace(" ", "")
    for char in string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            specials += 1
    return alphabets, digits, specials

string = "Hello World@"
alphabets, digits, specials = count_char(string)
print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special Characters:", specials)