class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        f = float('-inf')
        s = float('-inf')
        t = float('-inf')
        m1 = float('inf')
        m2 = float('inf')
        for num in nums:
            if num<m1:
                m2 = m1
                m1 = num
            elif num<m2:
                m2 = num
            if num > f:
                t = s
                s = f
                f = num
            elif num > s:
                t = s
                s = num
            elif num > t:
                t = num
        return max(f*s*t,m1*m2*f)