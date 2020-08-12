def insertion_sort(array):
    count = 0
    for i in range(1, len(array)):
        print(array)
        last_sorted_position = array[i-1]  #We store the last element which is sorted
        count += 1
        if array[i] < last_sorted_position: #We check if the current element is lesser than the last sorted element
            temp = array[i] #If yes, we store the curent element in a temporary variable.
            for j in range(i-1,-1,-1):  #We loop backwards through the sorted part of the array to check where the current element fits
                count += 1
                if temp < array[j]: #For every element we find in the sorted part which is greater than the current element, we shift them one place towards right to make room for the current element
                    if j == 0: #If we reach the beginning of the array in the process, we shift the elements right and we assign the current element to the 0th position
                        array[j+1] = array[j]
                        array[j] = temp
                    else: #Otherwise we just keep shifting
                        array[j+1] = array[j]
                else: #Once we find an element that is smaller than the current element, it means we have found the position to insert out current element at
                    array[j+1] = temp #So we just assign the element to its correct position
                    break #And break out of this loop
    return (f'{array} \nNumber of comparisons = {count}')

arr = [5,9,3,10,45,2,0]
print(insertion_sort(arr))
