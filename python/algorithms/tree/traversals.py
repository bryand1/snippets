def preorder(node):
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)

