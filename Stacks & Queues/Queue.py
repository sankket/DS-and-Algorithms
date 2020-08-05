# Queues can be implemented with array but it wont be efficient while pop process.
# Because FIFO principal we should use linked list.

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, data):
        new_node = Node(data)
        if self.last is  None:
            self.last = new_node
            self.first = self.last
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
    def dequeue(self):
        if self.first is None:
            print("The Queue is Empty")

        if self.last == self.first:
            self.last = None
            self.first = self.first.next
            self.length -= 1
            return self

    def print_queue(self):
        if self.last is None:
            print("Queue is Empty")
        else:
            current_node = self.first
            while current_node is not None:
                if current_node.next is None:
                    print(current_node.data)
                else:
                    print(f'{current_node.data}  <<--  ', end='')
                current_node = current_node.next



if __name__ == '__main__':

    my_queue = Queue()

    my_queue.enqueue("This")
    my_queue.enqueue("is")
    my_queue.enqueue("Queue")
    my_queue.dequeue()
    my_queue.print_queue()
    

    my_queue.peek()
    my_queue.print_queue()

    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.print_queue()



