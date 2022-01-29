class Solution:
    
    # Runtime: 79ms
    # Space: 14MB
    def romanToIntMain(self, s: str) -> int:
        myDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for i in range(len(s)-1,-1,-1):
            if 4 * myDict[s[i]] < result: result -= myDict[s[i]]
            else: result += myDict[s[i]]
        return result
    
    # Runtime: 104ms
    # Space: 13.9MB
    def romanToIntReplace(self, s: str) -> int:
        myDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        s = s.replace('IV','IIII').replace('IX','VIIII')
        s = s.replace('XL','XXXX').replace('XC','LXXXX')
        s = s.replace('CD','CCCC').replace('CM','DCCCC')
        result = 0
        for i in s:
            result += myDict[i]
        return result
    
    # Runtime: 77ms
    # Space: 13.8MB
    def romanToIntSimple(self, s: str) -> int:
        myDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prev, result = 0,0
        for i in s:
            result = result + myDict[i] - prev - prev if myDict[i] > prev else result + myDict[i]
            prev = myDict[i]
        return result