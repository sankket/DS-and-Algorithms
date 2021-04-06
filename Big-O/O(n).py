import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla']
large = ['nemo' for i in range(100000)]
def find_nemo(array):
    t0 = time.time()
    for i in range(0,len(array)):
        if array[i] == 'nemo':
            print("Found Nemo!!")
    t1 = time.time()
    print(f'The search took {t1-t0} seconds.')
find_nemo(nemo)
find_nemo(everyone)
find_nemo(large)


def funchallenge(input):
    temp = 10 
    temp = temp +50 
    for i in range(len(input)):
        var = True 
        a += 1 
    return a 

funchallenge(nemo)
funchallenge(everyone)
funchallenge(large)

#Here in the function the only one loop is used and therefore the complexity for this is O(n)
