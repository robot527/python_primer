#! usr/bin/python3

''' Two different implementations of fibonacci sequence
have different performance. '''

import time


def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


known = {0: 0, 1: 1}
def fib2(n):
    if n in known.keys():
        return known[n]
    res = fib2(n - 1) + fib2(n - 2)
    known[n] = res
    return res


def test_fib(func, para):
    now = time.clock()
    result = func(para)
    print('Elapsed time:', time.clock() - now)
    return result


'''print the first n items.'''
def fib_show(n):
    x, y = 0, 1
    count = 2
    print(x, y, end=' ')
    while count < n:
        x, y = y, x + y
        count += 1
        print(y, end=' ')
    print('\n')


if __name__ == '__main__':
    num = 32
    print('fib1(%d) = %d\n' % (num, test_fib(fib1, num)))
    print('fib2(%d) = %d\n' % (num, test_fib(fib2, num)))
    fib_show(num + 1)
