class Solution:
    
    # Run Time: 48ms
    # Space: 13.9MB
    
    def isValidReplace(self, s: str) -> bool:
        while len(s) > 0:
            l_before = len(s)
            s = s.replace('()','').replace('[]','').replace('{}','')
            if l_before == len(s):
                return False
        return not bool(s)
   

    # Run Time: 32ms
    # Space: 13.9MB
    
    def isValidSimple(self, s: str) -> bool:
        stack, s = [], list(s)
        myDict = {'{': '}', '[': ']', '(': ')'}
        for i in s:
            if i in myDict: stack.append(i)
            else:
                if not stack or myDict[stack.pop()] != i:
                    return False
        return not stack