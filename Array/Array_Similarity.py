# Check whether the 2 array contain same element.
# The Brute force approach where each element is compared with another.
# Here we applied two methods for array similarity.
n1 = int(input("Enter the number of elements for 1 :"))
array1 = []
for i in range(0, n1):
    ele1 = int(input())
    array1.append(ele1)
n2 = int(input("Enter the number of elements for 2 :"))
array2 = []
for i in range(0, n2):
    ele2 = int(input())
    array2.append(ele2)



def arraymatch(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                return print(True)

    return print(False)

arraymatch(array1,array2)


# this approach is better as it doesnt contain any nested loops.
n1 = int(input("Enter the number of elements"))
array1 = []
for i in range(0,n1):
    ele1=(input())
    array1.append(ele1)
n2 = int(input("Enter the number of elements for 2"))
array2 = []
for i in range(0,n2):
    ele2=(input())
    array2.append(ele2)

def arrayMatch(arr1,arr2):
    dictionery = dict()
    for i in range(len(arr1)):
        dictionery(arr1[i]==True)

    for i in range(len(arr2)):
        if(arr2[i] in dictionery):
            return print(True)
    return False
arrayMatch(array1,array2)

