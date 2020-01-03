from Empty import Empty

class Queue:

    def __init__(self):
        self._size = 0
        self._front = 0
        self._cap = 2
        self._data = [None] * self._cap

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            raise Empty('no data')
        return self._data[self._front]

    def _resize(self, order):
        if order == 'up':
            self._cap *= 2
        if order == 'dn':
            self._cap //= 2
        old = self._data
        self._data = [None] * self._cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % self._cap
        self._front = 0

    def enque(self, e):
        if self._size == self._cap:
            self._resize('up')
        self._data[(self._front + self._size) % self._cap] = e
        self._size += 1

    def deque(self):
        if self.is_empty():
            raise Empty('no data')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        self._front = (self._front + 1) % self._cap
        if self._size == self._cap // 4:
            self._resize('dn')
        return answer
