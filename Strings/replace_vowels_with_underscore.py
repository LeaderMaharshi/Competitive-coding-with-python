
def replace_first_vowel(s):
    vowels = "aeiouAEIOU"
    for i in range(len(s)):
        if s[i] in vowels:
            return s[:i] + "_" + s[i+1:]
    return s

s = "Hello world"
print(replace_first_vowel(s))