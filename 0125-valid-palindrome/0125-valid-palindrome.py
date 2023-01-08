class Solution:
    def isPalindrome(self, s: str) -> bool:
        newSter = ""
        for c in s:
            if c.isalnum():            
                newSter += c.lower()
        return newSter == newSter[::-1]