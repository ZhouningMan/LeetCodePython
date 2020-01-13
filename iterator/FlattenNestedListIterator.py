# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Pair:
    def __init__(self, li, index):
        self.li = li
        self.index = index

    def done(self):
        return self.index == len(self.li)

    def next(self):
        val = self.li[self.index]
        self.index += 1
        return val

    def isInt(self):
        return self.li[self.index].isInteger()

class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = [Pair(nestedList, 0)]

    def next(self):
        val = self.stack[-1].next()
        return val.getInteger()

    def hasNext(self):
        stack = self.stack
        while stack:
            pair = stack[-1]
            if pair.isInt():
                return True
            val = pair.next()
            if pair.done():
                stack.pop()
            stack.append(Pair(val.getList(), 0))
        return False

if __name__ == '__main__':
