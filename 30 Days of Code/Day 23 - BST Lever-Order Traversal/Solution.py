"""
@author: zepman85
"""

import sys

class Node:
    def __init__(self,data):
        self.right = self.left = None
        self.data = data
        
class Solution:
    def insert(self,root,data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root
    
    def __init__(self):
        self.nodeQueue = []

    def printDataAndEnqueueChildren(self, node):
        print(node.data, end = '')
        if node.left != None:
            self.nodeQueue.append(node.left)
        if node.right != None:
            self.nodeQueue.append(node.right)

        if len(self.nodeQueue) != 0:
            print(' ', end='')

    def levelOrder(self, root):
        self.nodeQueue = [root]
        while len(self.nodeQueue) != 0:
            cur = self.nodeQueue.pop(0)
            self.printDataAndEnqueueChildren(cur)
        

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
