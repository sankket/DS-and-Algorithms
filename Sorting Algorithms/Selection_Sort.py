# Here in selection sort we find the smallest element in the list.
# Then this smallest element will be swapped with leftmost element.
# Time complexity - O(n^2)


def selection_sort(array):
    count = 0
    for i in range(len(array)-1):
        print(array)
        min = array[i]
        min_index = i
        for j in range(i+1, len(array)):
            count += 1
            if array[j] < min:
                min = array[j]
                min_index = j
        if min_index != i:
            array[min_index], array[i] = array[i], array[min_index]
    return f'{array}\n Number of Counts :{count}'


arr = [23,2,43,22,1,56,76]

print(selection_sort(arr))

arr_sorted = [1,2,3,4,5,6]
print(selection_sort(arr_sorted))

