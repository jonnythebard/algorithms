import ctypes


class DynamicArray:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self._array = self._make_array(self.capacity)

    def __len__(self):
        return n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError(f"index {k} is out of bound")

    def _make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def _resize(self, new_cap):
        new_array = self._make_array(new_cap)

        for idx in range(self.n):
            new_array[idx] = self._array[idx]

        self._array = new_array
        self.capacity = new_cap

    def append(self, element):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        self._array[self.n] = element
        self.n += 1


if __name__ == "__main__":
    arr = DynamicArray()
    for n in range(6):
        arr.append(n)

    print(f"len: {len(arr)}")

    for n in range(len(arr)):
        print(n)