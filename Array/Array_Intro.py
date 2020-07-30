#Arrays are one of the most commonly-used data structures
#The elements of an array are stored in contiguous memory locations
#Arrays are of two types : Static and Dynamic
#Static arrays have fixed, pre-defined amount of memory that they can use, whereas in dynamic arrays this is flexible
Array = ['a', 'b', 'c', 'd', 'e']
first =Array[0]
last = Array[4]

Array.insert(2, 'x')

Array.remove('x')

Array.count('a')
#Push/Pop
#Push corresponds to pushing or adding an element at the end of the array.
#Similarly, pop corresponds to removing the element at the end of the array.

Array.append('s')

Array.reverse()

#Array.pop(1)

print(Array)
print(first, last)

