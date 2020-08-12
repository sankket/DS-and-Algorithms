# In bubble sort after every iteration the largest element will bubble towards the highest index position.
# Every 2 adjacent elements are compared and swapped when are not in order.
# Worst and average case - O(n^2) and for best Case O(n).


def bubble_sort(array):
    count = 0
    for i in range(len(array)-1):
        print(array)
        for j in range(len(array)-i-1):
            count += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return f'{array} \n Number of comparisons = {count}'


arr = [23,2,43,22,1,56,76]
print(bubble_sort(arr))
sorted_arr = [1,2,3,4,5,6]
print(bubble_sort(sorted_arr))

def bubble_sort_opt(array):
    count = 0
    for i in range(len(array)-1):
        swap = False
        print(array)
        for j in range(len(array)-i-1):
            count += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True
            if swap is False:
                return f'{array} \n Number of comparisons = {count}'

    return f'{array} \n Number of comparisons = {count}'


sorted_arr = [1,2,3,4,5,6]
print(bubble_sort_opt(sorted_arr))
