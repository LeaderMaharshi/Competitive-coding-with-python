string = "Hello World"

string = string.replace(" ", "").lower()

vowels = "aeiou"

vowel_count = 0
consonent_count = 0

for char in string:
    if char not in vowels:
        consonent_count += 1
    else:
        vowel_count += 1

print(f"Vowel count is: {vowel_count} \nconsonent count is: {consonent_count}")