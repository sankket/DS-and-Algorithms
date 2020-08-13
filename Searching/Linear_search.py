# Linear Search is basically simplest searching algorithm in which
# The target element will matched with all the element in the list.


def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return "The Target Found"
    else:
        return "Target is not Present"


array = [1, 4, 3, 27, 9, 7, 55, 66]

print(linear_search(array, 4))

