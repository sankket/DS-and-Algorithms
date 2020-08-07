# Binary search is non linear hierarchical data structure.
# Time complexities in most cases is O(log n).

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.num_of_nodes = 0

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.num_of_nodes += 1
            return self
        else:
            current_node = self.root
            while(current_node.left != new_node) and (current_node.right != new_node):
                if new_node.data > current_node.data:
                    if current_node.right is None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
                self.num_of_nodes += 1
                return self

    def lookup(self, data):
        if self.root is None:
            print("Tree is Empty")
        else:
            current_node = self.root
            while True:
                if current_node is None:
                    return "not Found"
                elif current_node.data == data:
                    return "Found"
                elif current_node.data > data:
                    current_node.data = current_node.left
                elif current_node.data < data:
                    current_node.data = current_node.right

    def remove(self, data):
        if self.root is None:
            return "Tree is empty"
        current_node = self.root
        parent_node = None
        while current_node is not None:
            if current_node.data > data:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.right is None:
                    if parent_node is None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return

                elif current_node.left is None:
                    if parent_node is None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.left
                            return

                elif current_node.left is None and current_node.right is None:
                    if parent_node is None:  # Node to be deleted is root
                        current_node = None
                        return
                    if parent_node.data > current_node.data:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return

                elif current_node.left is not None and current_node.right is not None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left is not None:
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.data = del_node.data  # The value to be replaced is copied
                    if del_node == del_node_parent:  # If the node to be deleted is the exact right child of the current node
                        current_node.right = del_node.right
                        return
                    if del_node.right is None:  # If the leftmost node of the right subtree of the current node has no right subtree
                        del_node_parent.left = None
                        return
                    else:  # If it has a right subtree, we simply link it to the parent of the del_node
                        del_node_parent.left = del_node.right
                        return
                return "Not Found"

        my_bst = BST()
        my_bst.insert(5)
        my_bst.insert(3)
        my_bst.insert(7)
        my_bst.insert(1)
        my_bst.insert(13)
        my_bst.insert(65)
        my_bst.insert(0)
        my_bst.insert(10)
        my_bst.lookup(444)

        my_bst.remove(65)

