class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        if not str:
            raise ValueError("...")
        dummy = Node(None)
        curr = dummy
        seen = set()
        # since we only use next
        # we store the previous node
        node_map = {}
        for c in str:
            if c in seen:  # found duplicate
                # special case
                if c not in node_map:
                    continue
                node = node_map[c]  # get the previous node
                node.next = node.next.next
                del node_map[c]
            else:
                # special case
                if len(node_map) == 0:  # reset
                    curr = dummy
                node_map[c] = curr  # save previous node for key c
                curr.next = Node(c)
                curr = curr.next
                seen.add(c)
        # we were told there exists a answer.
        return dummy.next.val

if __name__ == '__main__':
    s = Solution()
    ans = s.firstUniqChar('aaab')
    print(ans)