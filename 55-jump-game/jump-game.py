class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #Initially the final position is the last index
        last_position  = len(nums)-1
        # 4

        #   If you can reach the final position from this index
        #    update the final position flag
#              (4,-1 loop runm -1 decrement)
        for i in range(len(nums)-1,-1,-1):
            # mus[i ]  = jump length 
            if i + nums[i] >= last_position: 
               last_position = i 

        return last_position == 0


        