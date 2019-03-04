# Binary Search Tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def search(root, key):
    if root is None:
        return False
    
    if root.val == key:
        return root

    if key < root.val:
        return search(root.left, key)
    
    return search(root.right, key)


def insert(root, key):
    if root is None:
        return Node(key)

    if root.val == key:
        return root

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right)


def min_node(root):
    curr = root
    while curr.left is not None:
        curr = curr.left
    return curr


def max_node(root):
    curr = root
    while curr.right is not None:
        curr = curr.right
    return curr


def delete(root, key):
    if not root:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min_node(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)    
    return root


if __name__ == '__main__':
    # Driver program to test the above functions 
    # Let us create the following BST 
    #      50 
    #    /    \ 
    #   30     70 
    #   / \    / \ 
    #  20 40  60 80 
    r = Node(50) 
    insert(r, 30) 
    insert(r, 20) 
    insert(r, 40) 
    insert(r, 70) 
    insert(r, 60) 
    insert(r, 80)
    insert(r, 80)
    
    print('Inorder traversal of the BST')
    inorder(r)
    print()

    print('Search for node with value 20')
    s1 = search(r, 20)
    print(s1.val if s1 else None)
    print()

    print('Search for node that does not exist')
    s2 = search(r, 316)
    print(s2)

    print('Delete values 20, 30, and 40')
    delete(r, 20)
    delete(r, 30)
    delete(r, 40)
    inorder(r)
    print()

    print('Get maximum value in BST')
    print(max_node(r).val)
