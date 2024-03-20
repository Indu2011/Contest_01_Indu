class Solution:
    def productExceptSelf(self, arr, n):
        if n == 1:
            return [1]
        
        i, curr = 1, 1
        prod = [1 for i in range(n)]
        for i in range(n):
            prod[i] = curr
            curr *= arr[i]

        curr = 1
        for i in range(n - 1, -1, -1):
            prod[i] *= curr
            curr *= arr[i]
    
        return prod