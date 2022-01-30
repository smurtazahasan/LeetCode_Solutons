class Solution:
    
    # Runtime: 114ms
    # Space: 15.1MB
    def isPalindrome(self, s: str) -> bool:
        a, b = 0, len(s) - 1
        s = list(s.lower())
        while a < b:
            if not s[a].isalnum(): a += 1
            elif not s[b].isalnum(): b -= 1
            elif s[a] == s[b]:
                a += 1
                b -= 1
            else:
                return False
        return True
    
    # Runtime: 100ms
    # Space: 14.4MB
    def isPalindromeforloop(self, s: str) -> bool:
        l, s = '', s.lower()
        for i in s:
            l = l + i if i.isalnum() else l
        return l == l[::-1]

    # Runtime: 100ms
    # Space: 14.4MB
    def isPalindromeSimple(self, s: str) -> bool:
        l = [l + i.lower() for i in s if i.isalnum()]
        return l == l[::-1]