from doubly_linked_base import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, element, predecessor, successor):
        node = super()._insert_between(element, predecessor, successor)
        return self._make_position(node)

    def add_first(self, element):
        return self._insert_between(element, self._header, self._header._next)

    def add_last(self, element):
        return self._insert_between(element, self._trailer._prev, self._trailer)

    def add_before(self, position, element):
        original = self._validate(position)
        return self._insert_between(element, original._prev, original)

    def add_after(self, position, element):
        original = self._validate(position)
        return self._insert_between(element, original, original._next)

    def delete(self, position):
        original = self._validate(position)
        return self._delete_node(original)

    def replace(self, position, element):
        original = self._validate(position)
        old_value = original._element
        original._element = element
        return old_value


if __name__ == '__main__':
    L = PositionalList()

    p = L.add_last(8)
    q = L.add_after(p, 9)
    print(p.element())
