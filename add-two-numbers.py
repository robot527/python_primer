#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

refer
https://leetcode-cn.com/problems/add-two-numbers/solution/python3-by-chen-hao-9/
"""

from __future__ import print_function


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        n = l1.val + l2.val
        # print(type(n))
        l3 = ListNode(n % 10)
        l3.next = ListNode(n // 10)
        p1 = l1.next
        p2 = l2.next
        p3_prev = l3
        p3 = l3.next
        while True:
            if p1 and p2:
                sum = p1.val + p2.val + p3.val
                p3.val = sum % 10
                p3.next = ListNode(sum // 10)  # save carry to next node
                p1 = p1.next
                p2 = p2.next
                p3_prev = p3
                p3 = p3.next
            elif p1 and not p2:
                sum = p1.val + p3.val
                p3.val = sum % 10
                p3.next = ListNode(sum // 10)
                p1 = p1.next
                p3_prev = p3
                p3 = p3.next
            elif not p1 and p2:
                sum = p2.val + p3.val
                p3.val = sum % 10
                p3.next = ListNode(sum // 10)
                p2 = p2.next
                p3_prev = p3
                p3 = p3.next
            else:
                if p3.val == 0:  # last node of l3
                    p3_prev.next = None  # discard this node
                break
        return l3


# 将倒数第一位放在第一个node，倒数第二位放在第二个node，依此类推。
def gen_list_by_num_str(num):
    lst = ListNode(int(num[-1]))
    p = lst
    for i in range(2, len(num) + 1):
        q = ListNode(int(num[-i]))
        p.next = q
        p = q
    return lst


def print_num_list(lst):
    p = lst
    num = ""
    while p:
        num = str(p.val) + num  # 将高位数字放在低位数字之前
        p = p.next
    print(num)


if __name__ == '__main__':
    import sys

    argc = len(sys.argv)
    if argc != 3:
        print('Usage: python', sys.argv[0], 'N1 N2')
    else:
        n1 = gen_list_by_num_str(sys.argv[1])
        n2 = gen_list_by_num_str(sys.argv[2])
        # print_num_list(n1)
        # print_num_list(n2)
        sol = Solution()
        result = sol.addTwoNumbers(n1, n2)
        print_num_list(result)
        print(long(sys.argv[1]) + long(sys.argv[2]), "is sum of long integers.")
