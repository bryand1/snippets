class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree:

    def insert(self, root, key):
        # Step 1: Perform normal BST insert
        if root is None:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2: Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Get balance factor
        balance = self.get_balance(root)

        # Step 4: Handle based on case
        # Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)

        # Right Right
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)

        # Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_minimum(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, minval)
        
        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left) + self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

    def left_rotate(z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Recalculate height
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def right_rotate(z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Recalculate height
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return root.left - root.right

    def get_minimum(self, root):
        if root is None or root.left is None:
            return root
        return self.get_minimum(root.left)

    def preorder(root):
        if root:
            print("%d ", root.val, end="")
            self.preorder(root.left)
            self.preorder(root.right)

if __name__ == '__main__':
    tree = AVL_Tree()
    root = None
    nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for num in nums:
        root = tree.insert(num)

    # Preorder Traversal
    print("Preorder traversal after insertions:")
    tree.preorder(root)
    print()

    # Delete
    key = 10
    root = tree.delete(key)

    # Preorder Traversal
    print("Preorder traversal after deletion -")
    tree.preorder(root)
    print()

