# Binary Search follows divide and Conquer approach.

pos = -1


def binary_search(arr, num):

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == num:
            globals()['pos'] = mid
            return True

        else:
            if arr[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
    return False


array = [1, 5, 6, 11, 12, 22, 23]
n = 1

print(binary_search(array, n))


