class Node(object):

    def __init__(self, value):
        self.value = value

class SingleLinked(object):

    def __init__(self, s_next):
        self.s_next = Node(s_next)

    def insert(self, data):
        if Node.value == data:
            return False
        else:
            if self.s_next:
                return self.s_next.insert(data)
            else:
                self.s_next = Node(data)
                return True

class DoubleLinked(object):

    def __init__(self, d_prev, d_next):
        self.prev = Node(d_prev)
        self.d_next = Node(d_next)

    def insert(self, data):
        if Node.value == data:
            return False
        else:
            if self.d_next:
                return self.d_next.insert(data)
            else:
                self.d_next = Node(data)
                return True

class BinaryTree(object):

    def __init__(self, root, left, right):
        self.root = Node(root)
        self.left = Node(left)
        self.right = Node(right)

    def insert(self, data):
        if Node.value == data:
            return False
        elif Node.value > data:
            if self.left:                      
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True
