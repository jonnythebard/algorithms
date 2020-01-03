from doublylinkedbase import _DoublyLinkedBase

class Deque(_DoublyLinkedBase):

    def first(self):
        return self._header.next.element

    def last(self):
        return self._trailer.prev.element

    def insert_first(self, e):
        if self.is_empty():
            self._insert_between(e, self._header, self._trailer)
        else:
            self._insert_between(e, self._header, self._header.next)

    def insert_last(self, e):
        if self.is_empty():
            self._insert_between(e, self._header, self._trailer)
        else:
            self._insert_between(e, self._trailer.prev, self._trailer)

    def del_first(self):
        self._delete_node(self._header.next)

    def del_last(self):
        self._delete_node(self._trailer.prev)

    def disp(self):
        cur = self._header.next
        while not cur == self._trailer:
            print(cur.element, end=' ')
            cur = cur.next
        print()

if __name__ == '__main__':
    ''' 1. first / 2. last / 3. insert_f / 4. insert_l / 5. del_f / 6. del_l '''
    D = Deque()
    n = 0
    while True:
        order = input('input:')
        if order == '1':
            D.first()
        elif order == '2':
            D.last()
        elif order == '3':
            D.insert_first(n)
            D.disp()
            n += 1
        elif order == '4':
            D.insert_last(n)
            D.disp()
            n += 1
        elif order == '5':
            D.del_first()
            D.disp()
            n -= 1
        elif order == '6':
            D.del_last()
            D.disp()
            n -= 1
        else:
            break