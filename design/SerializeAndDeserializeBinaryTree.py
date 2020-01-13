"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque

class Solution:
    def serialize(self, root):
        if not root:
            return ""
        content = ""
        queue = deque([root])
        while queue:
            head = queue.popleft()
            if head:
                content += str(head.val)
                queue.extend([head.left, head.right])
            else:
                content += '#'
            content += ','
        return content

    def deserialize(self, data):
        if not data:
            return None
        # create tree from data, first create nodes
        # and the build relationships
        nodes = self.create_nodes(data)
        m = len(nodes)
        pi = 0  # keep a pointer to parent location
        for i in range(m):
            if nodes[i] is not None:
                if pi*2 + 1 >= m: # point to left child
                    nodes[i].left = None
                else:
                    nodes[i].left = nodes[pi*2 + 1]

                if pi*2 + 2 >= m: # point to right child
                    nodes[i].right = None
                else:
                    nodes[i].right = nodes[pi*2 + 2]
                # only increment the pointer index when the nodes[i]
                # is not None, so that it consumed two nodes
                pi += 1
        return nodes[0]

    def create_nodes(self, data):
        elements = data.split(',')
        nodes = []
        for e in elements:
            if e == '':
                continue
            if e == '#':
                nodes += [None]
            else:
                nodes.append(TreeNode(int(e)))
        return nodes

class SolutionDFS:
    def serialize(self, root):
        if not root:
            return ""
        data = []
        self.preorder(root, data)
        return ','.join(data)

    def preorder(self, root, data):
        if not root: # need to include null node
            data.append('#')
            return
        data.append(str(root.val))
        self.preorder(root.left, data)
        self.preorder(root.right, data)

    def deserialize(self, data):
        if not data:
            return None
        nodes = self.create_nodes(data)
        return self.build_tree(nodes)

    def build_tree(self, nodes):
        if not nodes:
            return None
        root = nodes.popleft()
        if not root:
            return root
        root.left = self.build_tree(nodes)
        root.right = self.build_tree(nodes)
        return root

    def create_nodes(self, data):
        elements = data.split(',')
        nodes = deque()
        for e in elements:
            if e == '':
                continue
            if e == '#':
                nodes += [None]
            else:
                nodes.append(TreeNode(int(e)))
        return nodes

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = SolutionDFS()
    serialized = s.serialize(root)
    print(serialized)
    node = s.deserialize(serialized)
    print("Done")