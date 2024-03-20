class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        return bin(n).count('1')==1 and (n-1)%3 == 0