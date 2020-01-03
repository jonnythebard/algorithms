from Empty import Empty

class _DoublyLinkedBase:

    class _Node:
        __slots__ = 'element', 'prev', 'next'

        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, pre, succ):
        newnode = self._Node(e, pre, succ)
        pre.next = newnode
        succ.prev = newnode
        self._size += 1
        return newnode

    def _delete_node(self, node):
        if self.is_empty():
            raise Empty('no data')
        tmp = node
        node.prev.next = tmp.next
        node.next.prev = tmp.prev
        del tmp