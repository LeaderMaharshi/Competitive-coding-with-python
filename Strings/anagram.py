
string1 = "listen"
string2 = "silent"

#remove spaces and make it lower

string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

#convert into list

string1_list = list(string1)
string2_list = list(string2)

# sort the list

string1_list.sort()
string2_list.sort()

if string1_list == string2_list:
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")