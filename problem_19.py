class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = 0
        length = 0
        maxi = 0
        for i in range(len(s)):
            if s[i] not in s[index:i]:
                maxi = max(maxi,i-index+1)
            else:
                while s[index]!=s[i]:
                    index+=1
                index+=1
        maxi = max(length,maxi)
        return maxi