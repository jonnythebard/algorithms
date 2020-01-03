from array_stack_prac import Stack

def matching_pharens(st):
    op = '({['
    cl = ')}]'
    S = Stack()
    for i in st:
        if i in op:
            S.push(i)
        elif i in cl:
            if S.is_empty():
                return False
            if cl.index(i) != op.index(S.pop()):
                return False
    return S.is_empty()

if __name__ == '__main__':
    print(matching_pharens('()((()))([]{})'))