from collections import OrderedDict

x = OrderedDict()
x['a'] = 1
x['b'] = 2
x['c'] = 3
x.move_to_end('a')
x.popitem(last=False)
print(x)
assert x == OrderedDict([('c', 3), ('a', 1)])

