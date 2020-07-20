"""Each node can be colored RED or BLACK."""
RED = "RED"
BLACK = "BLACK"


class NilNode(object):
    def __init__(self):
        self.color = BLACK


"""We define NIL to be the leaf sentinel of our tree."""
NIL = NilNode()


class Node(object):
    def __init__(self, key, color=RED, left=NIL, right=NIL, p=NIL):
        self.color = color
        self.key = key
        self.left = left
        self.right = right
        self.p = p


class Tree(object):
    def __init__(self, root=NIL):
        self.root = root


def left_rotate(T, x):
    """Left-rotates node x on tree T.

               x
              / \
             a   y
                / \
               b   g

    mutates into:

               y
              / \
             x   g
            / \
           a   b

    Used for maintaining tree balance.
    """
    y = x.right
    x.right = y.left
    if y.left != NIL:
        y.left.p = x
    y.p = x.p
    if x.p == NIL:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y


def right_rotate(T, x):
    """Right-rotates node x on tree T.

               x
              / \
             y   g
            / \
           a   b

    mutates into:

               y
              / \
             a   x
                / \
               b   g

    Used for maintaining tree balance.
    """
    y = x.left
    x.left = y.right
    if y.right != NIL:
        y.right.p = x
    y.p = x.p
    if x.p == NIL:
        T.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x
    x.p = y


def tree_insert(tree, z):
    """Inserts node 'z' into binary tree 'tree'."""
    y = NIL
    x = tree.root
    while x != NIL:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == NIL:
        tree.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def rb_insert(tree, x):
    """Does an insertion of 'x' into the red-black tree 'tree'.  The
    algorithm here is a little subtle, but is explained in CLR."""
    tree_insert(tree, x)
    x.color = RED
    while x != tree.root and x.p.color == RED:
        if x.p == x.p.p.left:
            y = x.p.p.right
            if y.color == RED:
                x.p.color = BLACK
                y.color = BLACK
                x.p.p.color = RED
                x = x.p.p
            else:
                if x == x.p.right:
                    x = x.p
                    left_rotate(tree, x)
                x.p.color = BLACK
                x.p.p.color = RED
                right_rotate(tree, x.p.p)
        else:
            y = x.p.p.left
            if y.color == RED:
                x.p.color = BLACK
                y.color = BLACK
                x.p.p.color = RED
                x = x.p.p
            else:
                if x == x.p.left:
                    x = x.p
                    right_rotate(tree, x)
                x.p.color = BLACK
                x.p.p.color = RED
                left_rotate(tree, x.p.p)
    tree.root.color = BLACK


def tree_minimum(x):
    """Returns the minimal element of the subtree rooted at 'x'."""
    while x.left != NIL:
        x = x.left
    return x


def tree_maximum(x):
    """Returns the maximal element of the subtree rooted at 'x'."""
    while x.right != NIL:
        x = x.right
    return x


def tree_successor(x):
    """Returns the inorder successor of node 'x'."""
    if x.right != NIL:
        return tree_minimum(x.right)
    y = x.p
    while y != NIL and x == y.right:
        x = y
        y = y.p
    return y


def tree_predecessor(x):
    """Returns the inorder predecessor of node 'x'."""
    if x.left != NIL:
        return tree_maximum(x.left)
    y = x.p
    while y != NIL and x == y.left:
        x = y
        y = y.p
    return y


def tree_height(node):
    """Returns the height of a subtree rooted by node 'node'."""
    if node == NIL:
        return 0
    return max(1 + tree_height(node.left), 1 + tree_height(node.right))


def tree_count_internal(node):
    """Returns the number of internal nodes in the subtree rooted at 'node'."""
    if node == NIL:
        return 0
    return 1 + tree_count_internal(node.left) + tree_count_internal(node.right)
