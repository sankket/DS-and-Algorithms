import time

array = ['a','b','c','d','e']

def log_all_pairs(array):
    for i in range(len(array)): 
        for j in range(len(array)): 
            print(array[i], array[j]) 

log_all_pairs(array)

# The code contains nested loops hence the complexity is O(n^2)
