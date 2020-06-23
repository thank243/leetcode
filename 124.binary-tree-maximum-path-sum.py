"""
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42
"""
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    max_sum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            lmr = node.val + left + right
            self.max_sum = max(self.max_sum, lmr)
            return node.val + max(left, right)

        dfs(root)
        return int(self.max_sum)


def sortlist(lis):
    length = len(lis)
    row = int(math.log2(length + 1))
    mapping = []
    result = []
    for _ in range(row):
        mapping.append([])
    for _ in range(length):
        result.append([])
    for i in range(row):
        n = 2 ** i
        while True:
            mapping[-i - 1].append(n)
            n += 2 ** (i + 1)
            if n > length:
                break
    n = 0
    for k in mapping:
        for v in k:
            result[v - 1] = lis[n]
            n += 1
    return result


def generator(tree):
    tree = sortlist(tree)
    if not tree:
        return None
    mid = len(tree) // 2
    root = TreeNode(tree[mid])
    root.left = generator(tree[:mid])
    root.right = generator(tree[mid + 1:])
    return root


x = generator([-10, 9, 20, int(), int(), 15, 7])
print(Solution.maxPathSum(Solution, x))
