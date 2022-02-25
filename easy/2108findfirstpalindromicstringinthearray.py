class Solution:
    
    # Runtime: 101ms
    # Memory Usage: 13.9MB
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]: return i
        return ""