class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        if not chars:
            return
        left = 0
        right = len(chars) - 1
        while left <= right:
            if chars[left].islower():
                left += 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                right -= 1
