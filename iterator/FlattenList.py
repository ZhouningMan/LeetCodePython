class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        if not nestedList:
            return []
        res = []
        itr_stack = []
        itr_stack.append(iter(nestedList))
        while itr_stack:
            curr = itr_stack[-1]
            element = next(curr, None)
            if element is None:
                itr_stack.pop()
            elif isinstance(element, list):
                itr_stack.append(iter(element))
            else:
                res.append(element)
        return res