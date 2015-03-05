#! usr/bin/python3

''' Different implementations of fibonacci sequence
have different performances. '''

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


def fib3(n):
    return n < 2 and 1 or fib3(n - 1) + fib3(n - 2)


fib4 = lambda n: n if n < 2 else fib4(n - 1) + fib4(n - 2)


def fib5(n):
    x, y = 0, 1
    while(n):
        x, y, n = y, x + y, n - 1
    return x


def fib6(n):
    def fib_iter(n, x, y):
        if 0 == n: return x
        else: return fib_iter(n - 1, y, x + y)
    return fib_iter(n, 0, 1)


fib7 = lambda n, x = 0,y = 1: x if not n else fib7(n - 1, y, x + y)


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
    print('fib5(%d) = %d\n' % (num, test_fib(fib5, num)))
    print('fib7(%d) = %d\n' % (num, test_fib(fib7, num)))
    fib_show(num + 1)
