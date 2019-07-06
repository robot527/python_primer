#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: luoyaozu

"""
https://leetcode-cn.com/problems/string-to-integer-atoi/
Implement atoi which converts a string to an integer.
"""


def my_atoi(s):
    import re
    return max(min(int(*re.findall(r'^[+-]?\d+', s.lstrip())), (1 << 31) - 1), -(1 << 31))


if __name__ == '__main__':
    print my_atoi("123")
    print my_atoi("   -32")
    print my_atoi("4193 with words")
    print my_atoi("words and 987")
    print my_atoi("-91283472332")
    print my_atoi("+91283472332236")
    print my_atoi("0xab")
    print my_atoi("ab")
