#! /usr/bin/python

'''
Calculate all prime numbers less than N.
'''

from __future__ import print_function

def is_prime(num):
    '''Determine whether num is a prime number.'''
    from math import sqrt
    if num < 2:
        return 0
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return 0
    return 1


def prime_number(num):
    '''Calculate all prime numbers less than num.'''
    prime_list = []
    for i in range(2, num):
        if is_prime(i) == 1:
            prime_list.append(i)
    return prime_list


if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    j = 0
    if argc != 2:
        print('Usage: ./prime_number.py N')
    else:
        for n in prime_number(int(sys.argv[1])):
            print(n, end='\t')
            j += 1
            if j % 8 == 0:
                print()
    print()
