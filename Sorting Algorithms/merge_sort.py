# Merge sort follows divide and Conquer Approach
# Where the list is divided into half until the single element remained
# and Merged back in sorted manner.
count = 0
def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array) // 2
        left_arr = array[:mid]
        right_arr = array[mid:]
        print(f'left :{left_arr}')
        print(f'right :{right_arr}')
        return merge(merge_sort(left_arr), merge_sort(right_arr))


def merge(left, right):
    l = len(left)
    r = len(right)
    left_index = 0
    right_index = 0
    sorted_arr = []

    while (left_index < l and right_index < r):
        global count
        count += 1
        if left[left_index] < right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1
    print(sorted_arr + left[left_index:] + right[right_index:])
    return sorted_arr + left[left_index:] + right[right_index:]


array = [32, 43, 5, 44, 78, 11, 23]
print(merge_sort(array))
