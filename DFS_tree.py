# Tree -- construction and DFS traversal algorithms

class Tnode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Tnode(20)
root.left = Tnode(10)
root.left.left = Tnode(5)
root.left.right = Tnode(15)
root.right = Tnode(30)
root.right.left = Tnode(25)
root.right.right = Tnode(35)

def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.value, end=' ')

def pre_order(root):
    if not root:
        return
    print(root.value, end=' ')
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.value, end=' ')
    in_order(root.right)

print("Post-order DFS traversal:")
post_order(root)

print("\nIn-order DFS traversal:")
in_order(root)

print("\nPre-order DFS traversal:")
pre_order(root)
