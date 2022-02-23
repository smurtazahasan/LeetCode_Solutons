class Solution:
    
    # Runtime: 53ms
    # Memory Usage: 13.8MB
    
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(2, len(s)):
            if s[i-2] != s[i-1] and s[i] != s[i-1] and s[i] != s[i-2]:
                count += 1
        return count