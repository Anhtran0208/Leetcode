"""
Problem:
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        children = set()
        for des in descriptions:
            parent = des[0]
            child = des[1]
            isLeft = des[2]
            if parent not in node_map:
                node_map[parent] = TreeNode(parent)
            if child not in node_map:
                node_map[child] = TreeNode(child)
            if isLeft == 1:
                node_map[parent].left = node_map[child]
            else:
                node_map[parent].right = node_map[child]
            children.add(child)
        for node in node_map.values():
            if node.val not in children:
                return node