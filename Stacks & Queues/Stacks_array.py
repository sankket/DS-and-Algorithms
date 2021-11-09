# stacks - data structure follows LIFO principal.
# stacks are linear data structure.in python the stacks can be implemeted with array and linked list.

class Stack:
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[len(self.array) - 1]

    def push(self,data):
        self.array.append(data)
        return

    def pop(self):
        if len(self.array) != 0:
            self.array.pop()
        else:
            print("Stack is Empty")

    def print_stacks(self):
        for i in range(len(self.array)- 1, -1, -1):
            print(self.array[i])
        return


if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push("Milan")
    my_stack.push("Madrid")
    my_stack.push("Paris")
    my_stack.push("Manchester")
    my_stack.push("London")

    my_stack.print_stacks()








