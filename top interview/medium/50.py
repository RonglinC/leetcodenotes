class Solution:
    def canJump(nums):
        length,right_most =len(nums),0
        for i in range(length):
            if i <=right_most:
                right_most =max(right_most,i+nums[i])
                if right_most >= length-1:
                    return True
        return False



