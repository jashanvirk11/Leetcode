class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        #  get the total numbers of rotation
        k = k % len(nums)

        # first reverse all list in array 
        # 7,6,5,4,3,2,1
        nums.reverse()

        # reverse first k element if k=3 
        # 7,6,5  7 is 0 index and k-1 is 2 index 
        # “self” we can access the attributes and methods of the class in Python. 
        self.reverse(nums, 0, k - 1)

         #REVERSE REMAINING ELEMENT
        self.reverse(nums, k, len(nums)-1)
        
    @staticmethod
    def reverse(nums,start,end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start +=1
            end -=1


         

