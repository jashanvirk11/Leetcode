class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)

        # last index  distination
        destination = len(nums) -1 
        # counter for jump
        times_of_jump = 0

        # record of current coverage , record of last jump index

        coverage,last_jump = 0,0

         # Quick response if start index == destination index == 0
        if size == 1:
            return 0
         # Greedy strategy: extend coverage as long as possible with lazy jump
        for i in range(0,size):
            # extend current coverage as further as possible
            coverage = max(coverage, i+nums[i])
            # forced to jump (by lazy jump) to extend coverage 
            if i == last_jump:
                 # update last jump index and increased by 1
                last_jump =coverage 
                times_of_jump +=1
                #  check if reached destination already
                if  coverage >= destination:
                    return times_of_jump




       

        