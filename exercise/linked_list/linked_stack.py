class Stack:

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.n = 0
        self.head = None

    def is_empty(self):
        return self.n == 0

    def push(self, value):
        node = self.Node(value)

        if self.n == 0:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        self.n += 1

    def pop(self):
        node = self.head
        self.head = node.next
        self.n -= 1
        return node

    def peek(self):
        if self.n > 0:
            return self.head.value
        else:
            print("no item")

    def size(self):
        return self.n

    def __str__(self):
        arr = []
        cursor = self.head
        while cursor is not None:
            arr.append(cursor.value)
            cursor = cursor.next

        return str(arr)


if __name__ == "__main__":
    stack = Stack()
    for n in range(6):
        stack.push(n)

    print(stack)

    for _ in range(3):
        stack.pop()

    print(stack)
    print(stack.size())
    print(stack.peek())
