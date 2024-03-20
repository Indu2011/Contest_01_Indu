class Solution:
    def subArrayExists(self,arr,n):
        dict = {0:-1}
        sum = 0
        for index,i in enumerate(arr):
            sum += i
            if sum in dict:
                return True
            dict[sum] = index
        return False