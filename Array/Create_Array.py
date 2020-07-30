#Although python has array in the form of list.
#We Will create our own Arrays.

class my_array():
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.length += 1
        self.data[self.length - 1] = item

    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item

    def insert(self,index,item):
        self.length += 1
        for i in range(self.length-1, index-1):
            self.data[i] = self.data[i-1]
        self.data[index] = item

    def delete(self,index):
        for i in range(index,self.length-1):
            self.data[i] = self.data[+1]
        del self.data[self.length-1]
        self.length -= 1

arr = my_array()
arr.push(1)
arr.push(3)
arr.push(6)
arr.push(9)

arr.pop()
print(arr.get(1))
print(arr)






