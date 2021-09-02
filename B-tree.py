class TreeNode:

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):

    if (not root):
        return

    inorder(root.left)
    print(root.val,end = " ")
    inorder(root.right)

root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(15)

print(root.val)
print(root.left.val)
print(root.right.val)

inorder(root)
