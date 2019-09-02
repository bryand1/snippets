from collections.abc import Hashable, MutableSequence, Sized

issubclass(list, MutableSequence)  # True


class SizedCollection:
    def __init__(self, size):
        self._size = size
    def __len__(self):  # Implementing __len__() is sufficient to be Sized
        return self._size


issubclass(SizedCollection, Sized)  # True


# Non-transitive Subclass Relationships
issubclass(object, Hashable)  # True
issubclass(list, object)      # True
issubclass(list, Hashable)    # False

