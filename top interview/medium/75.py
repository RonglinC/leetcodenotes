class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0,cur =0,0
        p2 = len(nums)-1
        while cur <= p2:
            if nums[cur] == 0:
                nums[p0],nums[cur] = nums[cur],nums[p0]
                p0+=1
                cur+=1
            elif nums[cur] == 2:
                nums[p2],nums[cur] = nums[cur],nums[p2]
                p2-=1
            else:
                cur+=1