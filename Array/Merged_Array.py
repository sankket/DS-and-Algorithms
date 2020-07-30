# Merge 2 Arrays.
def merged_array(array1, array2):
    new_array = []
    flag = 0
    first_array_index = 0
    second_array_index = 0

    while not (first_array_index >= len(array1) or second_array_index >= len(array2)):
        if array1[first_array_index] < array2[second_array_index]:
            new_array.append(array1[first_array_index])
            first_array_index += 1
        else:
            new_array.append(array2[second_array_index])
            second_array_index += 1
        if first_array_index == len(array1) - 1:
            flag = 1
    if flag == 1:
        for i in array2[second_array_index]:
            new_array.append(i)
    else:
        for i in array1[first_array_index]:
            new_array.append(i)

    return new_array


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8, 10, 12]

print(merged_array(arr1, arr2))

