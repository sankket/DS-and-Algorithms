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
