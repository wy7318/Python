class Node(object):
    def __init__(self, value):  #initiating node
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root): #initiate root of binary tree
        self.root = Node(root)

    def print_tree1(self, traversal_type):
        if traversal_type == "preorder": 
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root,"")
        elif traversal_type =="postorder":
            return self.postorder_print(tree.root,"")
        else:
            print("Traversal Type:"+str(traversal_type)+" is not supported")
            return False

    def preorder_print(self, start, traversal): #preorder : root>left>right
        if start:
            traversal += (str(start.value)+"-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal): #inorder: left>root>right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value)+"-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal): #postorder: left>right>root
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value)+"-")
        return traversal


#creating binary tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)

print(tree.print_tree1("preorder"))
print(tree.print_tree1("inorder"))
print(tree.print_tree1("postorder"))
