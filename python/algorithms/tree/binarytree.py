class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_symmetrical_recurse(tree):
    """
    A binary tree is symmetrical iff in its two branches, t1 and t2:
    1) t1.left is equal to t2.right
    2) t1.right is equal to t2.left
    :param tree: Binary tree
    :return: bool
    """

    def helper(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return helper(t1.left, t2.right) and helper(t1.right, t2.left)

    return helper(tree.left, tree.right)


def is_symmetrical_reverse(tree):
    """
    A binary tree is symmetrical if the reverse of its left branch is equal to its right branch
    :param tree: Binary tree
    :return: bool
    """

    def reverse(t):
        if t is None:
            return
        tmp = t.left
        t.left = reverse(t.right)
        t.right = reverse(tmp)
        return t

    def is_equal(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return is_equal(t1.left, t2.left) and is_equal(t1.right, t2.right)

    return is_equal(reverse(tree.left), tree.right)


if __name__ == '__main__':

    two = Node(2)
    # one = Node(1)
    # two.left = one
    four = Node(4)
    six = Node(6)
    eight = Node(8)

    three = Node(3)
    three.left = two
    three.right = four

    seven = Node(7)
    seven.left = six
    seven.right = eight

    root = Node(5)
    root.left = three
    root.right = seven

    print("Is symmetrical? {}".format(is_symmetrical_recurse(root)))
    print("Is symmetrical? {}".format(is_symmetrical_reverse(root)))
