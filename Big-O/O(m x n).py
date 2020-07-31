array1 = [1,2,3,4,5]
array2 = ['a','b','c','d','e']

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

