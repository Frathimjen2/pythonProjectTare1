class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert(root, newValue):
    if root is None:
        root = BinaryTreeNode(newValue)
        return root

    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        root.rightChild = insert(root.rightChild, newValue)
    return root


def height(root):
    if root == None:
        return 0

    hleft = height(root.leftChild)
    hright = height(root.rightChild)
    if hleft > hright:
        return hleft + 1
    else:
        return hright + 1


def CheckBalancedBinaryTree(root):
    if root == None:
        return True

    lheight = height(root.leftChild)
    rheight = height(root.rightChild)
    if (abs(lheight - rheight) > 1):
        return False
    lcheck = CheckBalancedBinaryTree(root.leftChild)
    rcheck = CheckBalancedBinaryTree(root.rightChild)
    if lcheck == True and rcheck == True:
        return True


root = insert(None, 15)
insert(root, 10)
insert(root, 25)
insert(root, 6)
insert(root, 14)
insert(root, 20)
insert(root, 60)
print("Imprime True si el Arbol binario esta equilibrado:")
print(CheckBalancedBinaryTree(root))