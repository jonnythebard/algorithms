def run_stack_test():
    from array_stack_prac import Stack
    print()

    S = Stack()
    num = 0

    def push():
        S.push(num)
        print('PUSH:', num, 'cap:', S._cap, 'size:', S._size, S._data)

    def pop():
        n = S.pop()
        print('POP:', n, 'cap:', S._cap, 'size:', S._size, S._data)

    while True:
        order2 = input('1.push / 2.pop / 3.quit :')
        if order2 == '1':
            push()
            num += 1
        elif order2 == '2':
            pop()
            num -= 1
        else:
            del S
            break

def run_queue_test():
    from array_queue_prac import Queue
    print()

    Q = Queue()
    num = 0

    def enque():
        Q.enque(num)
        print('PUSH:', num, 'cap:', Q._cap, 'size:',  Q._size,
              'first:', Q._front,'len:', len(Q._data), Q._data)

    def deque():
        n = Q.deque()
        print('POP:', n, 'cap:', Q._cap, 'size:', Q._size,
              'first:', Q._front, 'len:', len(Q._data), Q._data)

    while True:
        order2 = input('1.enque / 2.deque / 3.quit :')
        if order2 == '1':
            enque()
            num += 1
        elif order2 == '2':
            deque()
        else:
            del Q
            break

while True:

    print('    TEST \n'
          '1. STACK \n'
          '2. QUEUE \n'
          '3. DEQUEUE \n'
          '4. QUIT')

    order = input('Which one?:')

    if order == '1':
        run_stack_test()
    elif order == '2':
        run_queue_test()
    elif order == '4':
        break
    else:
        print('not supported\n')