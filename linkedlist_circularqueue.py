from Empty import Empty

class Circular_Queue:

    class _Node:
        def __init__(self, elemnet, next):
            self.element = elemnet
            self.next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def first(self):
        if self.is_empty():
            raise Empty('no data')
        return self._tail.element

    def is_empty(self):
        return self._size == 0

    def enque(self, e):
        if self.is_empty():
            newnode = self._Node(e, None)
            self._head = self._tail = newnode
            self._tail.next = self._head
        else:
            newnode = self._Node(e, self._head)
            self._tail.next = newnode
            self._tail = newnode
        self._size += 1

    def deque(self):
        if self.is_empty():
            raise Empty('no data')
        answer = self._head.element
        self._head = self._head.next
        self._tail.next = self._head
        self._size -= 1
        return answer

    def rotate(self):
        if self.is_empty():
            raise Empty('no data')
        elif self._size > 1:
            self._head = self._head.next
            self._tail = self._tail.next

    def disp(self):
        if self._size == 1:
            print(self._head.element)
        elif self._size > 1:
            tmp = self._head
            while not tmp.next == self._head:
                print(tmp.element, end=' ')
                tmp = tmp.next
            print(tmp.element)

if __name__ == '__main__':
    S = Circular_Queue()
    n = 0
    print('1. enque / 2. deque / 3. len / 4. rotate / 5. first / 6. exit')
    while True:
        order = input('input:')

        if order == '1':
            S.enque(n)
            S.disp()
            n += 1
        elif order == '2':
            print('deque:', S.deque())
            S.disp()
        elif order == '3':
            print(S.__len__())
        elif order == '4':
            S.rotate()
            S.disp()
        elif order == '5':
            print(S.first())
        else:
            break