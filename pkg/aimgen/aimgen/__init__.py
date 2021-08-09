from collections.abc import Hashable, MutableSet

class UserSet(Hashable, MutableSet):
    __hash__ = MutableSet._hash

    def __init__(self, iterable=()):
        self.data = set(iterable)

    def __contains__(self, value):
        return value in self.data

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)

    def add(self, item):
        self.data.add(item)

    def discard(self, item):
        self.data.discard(item)