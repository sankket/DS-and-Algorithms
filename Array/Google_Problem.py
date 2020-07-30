array = [1,2,3,4,5]

sum = 32
def eleSum(arr,sum):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == sum :
                return print("Yes")
    return print("NOPE")

eleSum(array,sum)
