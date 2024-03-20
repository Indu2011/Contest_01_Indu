from collections import Counter 
class Solution:
    def isPossible(self, S):
        a = Counter(S)
        a = dict(a)
        cnt = 0
        for i in a.values():
            if i%2==1:
                cnt+=1
        if cnt>1:
            return False
        return True