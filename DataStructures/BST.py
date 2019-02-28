class Node(object):
    def __init__(self, value):  #initiating node
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:                 #if data is less than the value of current node
            if self.left:                       #check if there is left child
                return self.left.insert(data)   #then insert into left child
            else:
                self.left = Node(data)          #if not, create new node using that data
                return True
        else:                                   #if data is greater than the value of current node
            if self.right:                      #check if there is right child
                return self.right.insert(data)  #then insert data
            else:
                self.right=Node(data)           #if not, create new node with data
                return True

    def find(self, data):
        if(self.value == data):
            return True
        elif self.value > data:                 #if data is less than the value of current node
            if self.left:                       #if left node exist
                return self.left.find(data)     #find left node
            else:
                return False
        elif self.value < data:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.value))
            if self.right:
                self.right.inorder()


class BinaryTree(object):
    def __init__(self):                   #initiate root of binary tree
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root == Node(data)
            return True

    def find(self, data):
        if self.root:                           #check if there is root already
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print("Preorder")
            self.root.preorder()

    def postorder(self):
        if self.root is not None:
            print("Postorder")
            self.root.postorder()

    def inorder(self):
        if self.root is not None:
            print("Inorder")
            self.root.inorder()


bst=BinaryTree()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(5)
bst.insert(6)
bst.insert(7)
print(bst)
bst.postorder()
