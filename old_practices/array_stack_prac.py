from Empty import Empty

class Stack:

    def __init__(self):
        self._cap = 2
        self._data = [None] * self._cap
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self._size == 0:
            raise Empty('no data')
        return self._data[-1]

    def push(self, e):
        if self._size == self._cap:
            self._resize('up')
        self._data[self._size] = e
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise Empty('no data')
        answer = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        if self._size == self._cap // 4:
            self._resize('dn')
        return answer

    def _resize(self, order):
        if order == 'up':
            self._cap *= 2
        elif order == 'dn':
            self._cap //= 2
        old = self._data
        self._data = [None] * self._cap
        walk = 0
        for i in range(self._size):
            self._data[i] = old[walk]
            walk += 1
