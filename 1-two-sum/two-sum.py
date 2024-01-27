class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store numbers and their indices
        hash_set = {}        
        # Enumerate through the list of numbers
        for index, number in enumerate(nums):
            # Calculate the complement of the current number
            y = target - number
            # If complement is in the index_map, a solution is found
            if y in hash_set:
                # Return the indices of the two numbers
                return [hash_set[y], index]
            # Otherwise, add the current number and its index to the index_map
            hash_set[number] = index
        # If no solution is found, this return will not be reached due to guaranteed solution.