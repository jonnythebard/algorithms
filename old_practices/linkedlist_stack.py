from Empty import Empty

class LinkedStack:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
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
    S = LinkedStack()
    n = 0
    print('1. push / 2. pop / 3. len / 4. is_empty / 5. exit')
    while True:
        order = input('input:')

        if order == '1':
            S.push(n)
            S.disp()
            n += 1
        elif order == '2':
            S.pop()
            S.disp()
            n -= 1
        elif order == '3':
            print(S.__len__())
        elif order == '4':
            print(S.is_empty())
        else:
            break