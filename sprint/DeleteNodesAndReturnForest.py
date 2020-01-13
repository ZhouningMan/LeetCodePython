# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        parentMap = {root: TreeNode(-1)}  # add a dummy parent for root
        deleteMap = {}
        self.buildMaps(root, parentMap, set(to_delete), deleteMap)

        roots = set()
        roots.add(root)
        for d in deleteMap.values():
            if d in roots:
                roots.remove(d)
            if d.left:
                roots.add(d.left)
            if d.right:
                roots.add(d.right)
            parent = parentMap[d]
            if parent.left == d:
                parent.left = None
            else:
                parent.right = None
        return roots

    def buildMaps(self, root, parentMap, toDelete, deleteMap):
        if not root:
            return
        if root.val in toDelete:
            deleteMap[root.val] = root
        if root.left:
            parentMap[root.left] = root
            self.buildMaps(root.left, parentMap, toDelete, deleteMap)
        if root.right:
            parentMap[root.right] = root
            self.buildMaps(root.right, parentMap, toDelete, deleteMap)

