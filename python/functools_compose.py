from functools import reduce


def compose(*functions):
    """https://mathieularose.com/function-composition-in-python/"""
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


mul_two = lambda x: 2 * x
add_one = lambda x: x + 1
add_two = lambda x: x + 2

"""
When representing a binary tree in an array, let the current node be i
Access the left child by 2 * i + 1
Access the right child by 2 * i + 2
If the result of either calculation is an index that exceeds the length
of the array, then the child does not exist
"""
left_child = compose(add_one, mul_two)
right_child = compose(add_two, mul_two)

root = 0
btree = [7, 3, 10, 1, 4, 9, 100]

print(btree[left_child(root)])
print(btree[right_child(root)])
