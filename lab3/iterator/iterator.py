class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

class BinaryTreeIterator:
    def __init__(self, root):
        self.stack = []
        self.push_left_branch(root)

    def push_left_branch(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def get_current_node(self) -> Node:
        return self.stack[-1]

    def next_node(self):
        if len(self.stack) == 1:
            raise Exception("No more nodes forward to iterate")
        current_node = self.stack.pop()
        if current_node.right:
            self.push_left_branch(current_node.right) # the leftest node of the right subtree is the next node

if __name__ == "__main__":
    tree = BinaryTree()
    values = [8,5,3,4,2,7,1]
    for v in values:
        tree.insert(v)

    iterator = BinaryTreeIterator(tree.root)
    
    while True:
        print(f"Current node value: ", iterator.get_current_node().value)
        try:
            iterator.next_node()
        except Exception as ex:
            print(ex.__str__())
        input()


