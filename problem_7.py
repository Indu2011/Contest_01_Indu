import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0: return False
        m = log10(n)/log10(3)
        print(m)
        return m==int(m)