import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # return num in {6, 28, 496, 8128, 33550336} based on given constraints
        if (num == 1):
            return False
        sum = 1
        for i in range(2,int(math.sqrt(num))+1):
            if (num % i == 0):
                sum += i + num / i
        return sum == num