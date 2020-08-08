string1 = str(input("Enter a string to reverse :"))


def reverse_string(string):
    string1 = ''
    for i in string:
        string1 = i + string1
    return string1


print("The original string : ", string1)

print("The reverse of the string: ", reverse_string(string1))

string2 = "my name is godbole"

print(string2[::-1])

def recursive_reverse(string):
    print(string)
    if len(string) == 0:
        return string
    else:
        return recursive_reverse(string[1:]) + string[0]


print(recursive_reverse("All is Well"))

