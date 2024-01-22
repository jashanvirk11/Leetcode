class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # length of the nums [1,2,3,4]
        length = len(nums)
        
        # length of products =  [1,1,1,1]
        products_left = [1]* length # initialize left_product array with 1
        products_right = [1]* length

        for i in range(1, length):
            products_left[i] = products_left[i-1]*nums[i-1]
           

            """
            product array is 

            [1, 1, 2, 6]
            """

        for i in range(length-2,-1,-1):
            products_right[i] = products_right[i+1] * nums[i+1]
        # print(products_right)
        # 24,12,8,6

    # calculate the product of all elements except nums[i]
        result = [1]* length
        for i in range(0, length):
            result[i] = products_left[i]*products_right[i]
           
        return result 
        