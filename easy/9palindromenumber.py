class Solution:
    
    # Run Time: 104ms
    # Space: 13.9MB
    def isPalindromePointers(self, x: int) -> bool:
        x = str(x)
        a, b = 0, len(x) - 1
        if x[a] == '-': return False
        while a < b:
            if x[a] == x[b]: a, b = a + 1, b - 1
            else: return False
        return True
    
    # Run Time: 133ms
    # Space: 14MB
    def isPalindromeModulus(self, x: int) -> bool:
        original, result = x, 0
        while x > 0:
            result = (result * 10) + (x % 10)
            x = x // 10
        return result == original
    
    # Run Time: 127ms
    # Space: 13.8MB
    def isPalindromeString(self, x: int) -> bool:
        if x < 0: return False
        return str(x) == str(x)[::-1]