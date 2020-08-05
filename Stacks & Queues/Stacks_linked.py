# stacks can also be implemeted with linked list.
class Node():
    def __init__(self ,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.data

    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
            self.bottom = new_node
            self.length += 1
        else:
            new_node.next = new_node
            self.top = new_node
            self.length += 1

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            self.top = self.top.next
            self.length -= 1
            if self.length == 0:
                self.bottom = None

    def print_stack(self):
        if self.top is None:
            print("Stack empty")
        else:
            current_pointer = self.top
            while current_pointer is not None:
                print(current_pointer.data)
                current_pointer = current_pointer.next



if __name__ == '__main__':

    my_stack = Stack()
    my_stack.push("Milan")
    my_stack.push("Madrid")
    my_stack.push("Barcalona")
    my_stack.push("Manchester")
    my_stack.push("London")

    my_stack.peek()

    my_stack.print_stack()





