import functools


class Cell:
    def __init__(self):
        self._alive = False
    @property
    def alive(self):
        return self._alive
    def set_state(self, state):
        self._alive = bool(state)
    set_alive = functools.partialmethod(set_state, True)
    set_dead = functools.partialmethod(set_state, False)


if __name__ == '__main__':
    c = Cell()
    print(c.alive)
    c.set_alive()
    print(c.alive)

