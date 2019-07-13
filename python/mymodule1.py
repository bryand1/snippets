import mymodule2

for attr_name in dir(mymodule2):
    attr = getattr(mymodule2, attr_name)
    if callable(attr):
        print(attr)
