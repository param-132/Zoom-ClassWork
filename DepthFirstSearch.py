#Assignment:
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
#Function for postorder
    def PostOrder(self, root):
        if root:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.data)
def prtLevelOrder(root):
    h = height(root)
    for i in range (1, h+1):
        prtLevel(root, i)
def prtLevel(root, level):
    if root is None:
        return
    if level==1:
        print(root.data)
    elif level>1:
        prtLevel(root.left, level-1)
        prtLevel(root.right, level-1)
 #function to define the height of the tree
def height(node):
    if node is None:
        return 0
    else :
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight> rheight:
            return lheight+1
        else :
            return rheight+1
root = Node(31)
root.left = Node(14)
root.right = Node(34)
root.left.left = Node(12)
root.left.right = Node(22)
root.right.left = Node(32)
root.right.right = Node(40)
root.left.left.left = Node(6)
root.left.left.left.left = Node(5)
root.right.right.left = Node(37)
root.right.right.right = Node(48)
root.left.right.left = Node(18)
root.left.right.right = Node(28)
print("Level order traversal of binary tree is:")
prtLevelOrder(root)
print("Post Order traversal is:")
root.PostOrder(root)