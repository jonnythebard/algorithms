from doublylinkedbase import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):

    # ------------ nested Position class ------------

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)


    # ---------------- utility method ----------------

    def _validate(self, p):

        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')

        if p._container is not self:
            raise ValueError('p does not belong to this container')

        if p._node.next is None:
            raise ValueError('p is no longer valid')

        return p._node

    def _make_position(self, node):

        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)


    # ------------------ accessors --------------------

    def first(self):
        return self._make_position(self._header.next)

    def last(self):
        return self._make_position(self._trailer.prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
        cursor = self.after(cursor)


    # ------------------- mutators -------------------

    def _insert_between(self, e, pre, succ):
        node = super()._insert_between(e, pre, succ)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header.next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer.prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original.prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original.next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original.element
        original.element = e
        return old_value


if __name__ == '__main__':
    L = PositionalList()

    p = L.add_last(8)
    q = L.add_after(p, 9)
    print(p.element())
    print(p._node.next.element)


