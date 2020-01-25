from .Empty import Empty


class LinkedQueue:

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('no data')
        return self._head._element

    def enqueue(self, e):
        newnode = self._Node(e, None)
        if self.is_empty():
            self._head = newnode
        else:
            self._tail._next = newnode
        self._tail = newnode
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('no data')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def disp(self):
        tmp = self._head
        while tmp:
            print(tmp._element, end=' ')
            tmp = tmp._next
        print()

if __name__ == '__main__':
    S = LinkedQueue()
    n = 0
    print('1. enque / 2. deque / 3. len / 4. is_empty / 5. first / 6. exit')
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
            print(S.is_empty())
        elif order == '5':
            print(S.first())
        else:
            break
