class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tot = 0
        srt = 0
        sol = float('inf')
        end = 0
        while end < len(nums):
            tot += nums[end]
            while tot >= target:
                sol = min(sol,end-srt+1)
                tot -= nums[srt]
                srt += 1
            end += 1
        return sol if sol != float('inf') else 0