# Python code to insert a node in AVL tree
# https://www.geeksforgeeks.org/avl-tree-set-1-insertion/

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree:

    def insert(self, root, key):
        """
        Recursive function to insert key in subtree rooted with node
        Returns new root of subtree
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        # Step 1: Perform normal BST insert
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        # Step 2: Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Get the balance factor
        balance = self.get_balance(root)
    
        # Step 4: If the node is unbalanced, then try out the 4 cases
        # Case 1: Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        
        # Case 2: Right Right
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        
        # Case 3: Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Case 4: Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y
    
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform the rotation
        y.right = z
        z.left = T3

        # Update heights
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
        return self.get_height(root.left) - self.get_height(root.right)
    
    def preorder(self, root):
        if root:
            print("%d " % root.val, end="")
            self.preorder(root.left)
            self.preorder(root.right)


if __name__ == '__main__':
    tree = AVL_Tree()
    root = None

    root = tree.insert(root, 10)
    root = tree.insert(root, 20)
    root = tree.insert(root, 30)
    root = tree.insert(root, 40)
    root = tree.insert(root, 50)
    root = tree.insert(root, 25)

    """The constructed AVL Tree would be 
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50"""
    
    # Preorder Traversal
    print("Preorder traversal of the constructed AVL tree is: ")
    tree.preorder(root)
    print()
