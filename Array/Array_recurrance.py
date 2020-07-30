#Print the element which occured more than one time in array.
def First_rec(array):
    dictionary = dict()

    for i in array:
        if i in dictionary:
            return i
        else:
            dictionary[i] = True
    return None


array = [2, 1, 4, 1, 6, 5, 1, 4]

print(First_rec(array))


