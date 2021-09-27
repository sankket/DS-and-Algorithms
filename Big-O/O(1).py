import time

nemo = ["sane", "mane", "salah", "nemo"]


def findnemo(array):
    start = time.time()
    for i in range(len(nemo)):
        print("Running")
        if (array[i] == "nemo"):
            print("Found Nemo")
            break
    end = time.time()

    print(f"Runtime of the program is {end - start}" + "miliseconds")


findnemo(nemo)
# This program will demonstrate how much time the code is taking.
# we are using only one loop hence the average case complexity is O(n) and best case is o(1).
# it will depend upon the loops whether complexity will get high or low.
