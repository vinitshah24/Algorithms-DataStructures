""" Binary Search Tree """


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def inorder(root):
    """print inorder tree traversal"""
    if root:
        inorder(root.left)
        print("{0} ".format(root.val), end="")
        inorder(root.right)


def search(root, key):
    if root is None:
        return False
    if root.val == key:
        return True
    if root.val > key:
        return search(root.left, key)
    elif root.val < key:
        return search(root.right, key)
    return False


# return the node with minum key value found in that tree.
def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete_node(root, key):
    if root is None:
        return root
    # If the key is smaller than root's key, it lies in left subtree
    if key < root.val:
        root.left = delete_node(root.left, key)
    # If the kye is greater than root's key, it lies in right subtree
    elif key > root.val:
        root.right = delete_node(root.right, key)
    # If key is same as root's key, then this is the node to be deleted
    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # Node with two children:
        # Get the inorder successor (smallest in the right subtree)
        temp = min_value_node(root.right)
        # Copy the inorder successor's content to this node
        root.val = temp.val
        # Delete the inorder successor
        root.right = delete_node(root.right, temp.val)
    return root


node = Node(50)
insert(node, Node(30))
insert(node, Node(20))
insert(node, Node(40))
insert(node, Node(70))
insert(node, Node(60))
insert(node, Node(80))
inorder(node)
print()
isExists = search(node, 70)
print(isExists)
node = delete_node(node, 30)
inorder(node)
print()
node = delete_node(node, 50)
inorder(node)
#       50
#     /   \
#    30    70
#   / \   / \
#  20 40 60 80
