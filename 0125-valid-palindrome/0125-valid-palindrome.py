class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ct="".join(char for char in s if char.isalnum()).lower()
        return ct[::-1]==ct