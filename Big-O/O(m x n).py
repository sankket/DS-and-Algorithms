array1 = [1,2,3,4,5,6]
array2 = ['a','b','c','d','e']

#Here we used nested loops in the fuunction pairs.
#Hence the Complexity for the code is O(n*m).

def pairs(array1, array2):
    for i in range(len(array1)):
        for j in range(len(array2)):
            print(array1[i], array2[j])

pairs(array1, array2)



def hiNtimes(n):
    hiArray = []
    for i in range(n):
        hiArray.append("HI")
    return print(hiArray)


hiNtimes(4)

