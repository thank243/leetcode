"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        tmp = ans
        tmpsum = 0
        while True:
            # 依次遍历l1 l2，对应位相加
            if l1:
                tmpsum += l1.val
                l1 = l1.next
            if l2:
                tmpsum += l2.val
                l2 = l2.next
            tmp.val = tmpsum % 10  # 除10取余作为当前位的值
            tmpsum //= 10  # 除10取整，即高位，作为指针的下个结点 进行加法运算
            if not l1 and not l2 and tmpsum == 0:
                break
            tmp.next = ListNode(0)
            tmp = tmp.next
        return ans

    def generateList(self, links: list) -> ListNode:
        prenode = ListNode(0)
        lastnode = prenode
        for val in links:
            lastnode.next = ListNode(val)
            lastnode = lastnode.next
        return prenode.next


Solution.generateList(Solution, [1, 2, 3, 4, 5])
