from Create_linked_list import linked_list, Node
my_linked_list = linked_list()

my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

my_linked_list.print_list()

def reverse(linked_list):
    if linked_list.length <= 1:
        return linked_list
    else:
        first = linked_list.head
        second = first.next
        linked_list.tail = linked_list.head
        while second:
            temp =second.next
            second.next = first
            first = second
            second = temp
        linked_list.head.next = None
        linked_list.head = first
        return linked_list


reversed_linked = reverse(my_linked_list)
reversed_linked.print_list()


