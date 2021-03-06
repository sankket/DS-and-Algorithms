class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
            return
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return


    def prepend(self, data):
        new_node = Node(data)
        if self.head is None :
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
            return


    def insert(self, index, data):
        if index >= self.length:
            if index > self.length:
                print("The position is not available, inserting at the end of the list")
            return self.append(data)

        if index == 0:
            return self.prepend(data)

        if index < self.length:
            new_node = Node(data)
            current_node = self.head

            for i in range(index - 1):
                current_node = current_node.next
            new_node.prev = current_node
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

    def delete(self, index):
        if self.head is None:
            print("The list is empty and you cant delete anything from it.")
        if index == 0:
            self.head = self.head.next
            if self.head is None or self.head.next is None:
                self.tail = self.head
                self.length -= 1
            if index >= self.length:
                index = self.length - 1
                current_node = self.head
                for i in range(index - 1):
                    current_node = current_node.next
                current_node.next = current_node.next.next
                self.length -= 1
                if current_node.next is None:
                    self.tail = current_node


    def print_list(self):
        if self.head is None:
            print("EMPTY")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=' ')
                current_node = current_node.next
        print()


if __name__ == '__main__':
    my_linked_list = doubly_linked_list()
    my_linked_list.print_list()
    my_linked_list.append(10)
    my_linked_list.append(5)
    my_linked_list.append(12)
    my_linked_list.prepend(3)

    my_linked_list.insert(2,33)
    my_linked_list.insert(9,56)
    my_linked_list.print_list()

    my_linked_list.delete(2)

    my_linked_list.print_list()


