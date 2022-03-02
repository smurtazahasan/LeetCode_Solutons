class Solution:
    
    # Runtime: 315ms
    # Memory Usage: 15MB
    
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l, result = 0, 0
        curr = 0
        import collections
        dq = collections.deque()
        
        for r in range(len(s)):
            dq.append(s[r])
            
            if s[r] in vowels:
                curr += 1
            
            if r >= k - 1:
                result = max(result, curr)
                if dq.popleft() in vowels: curr -= 1
        return result
                