''''class Node:
    def _init_(self,val):
        self.val=val
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        first=Node(1)
        second=Node(2)
        third=Node(3)
        fourth=Node(4)
        fifth=Node(5)
        Sixth=Node(6)
        seventh=Node(7)
        self.root=first
        first.left=second
        first.right=third
        second.left=fourth
        second.right=fifth
        third.left=Sixth
        third.right=seventh

    def PostOrder(self,root):
        if(root==None):
            return
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.val)

b=BST()'''
import self as self


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # A utility function to insert a new node with the given key




            # A utility function to do inorder tree traversal


    def inorder(root):
        if root:
            inorder(root.left)
            print(root.val)
            inorder(root.right)

    def postOrder(root):
        if(root):
            postOrder(root.left)
            postOrder(root.right)
            print(root.val)

    # Driver program to test the above functions


# Let us create the following BST
#      50
#    /      \
#   30     70
#   / \    / \
#  20 40  60 80
b=BST()
''''r=Node(50)'''''
b.insert(self.head,30)
''''b.insert(r, Node(20))'''
''''b.insert( Node(40))
b.insert( Node(70))
b.insert( Node(60))
b.insert(r, Node(80))''''

# Print inoder traversal of the BST
print("This is inorder")
''''inorder(r)
''''print("This is post Order\n\n")
''''postOrder(r)'''''

