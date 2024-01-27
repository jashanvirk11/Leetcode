class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """ 
          # Find the number of elements in height.
        num_elements = len(height)

        # Initialize arrays to store the maximum to the left and right of each element.
        max_left = [height[0]] * num_elements
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        max_right = [height[-1]] * num_elements
        # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        # Fill the max_left array with the maximum height to the left of each element.
        for i in range(1, num_elements):
            max_left[i] = max(max_left[i - 1], height[i])
            # [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            # [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            # [0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
            # [0, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0]
            # [0, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0]
            # [0, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0, 0]
            # [0, 1, 1, 2, 2, 2, 2, 3, 0, 0, 0, 0]
            # [0, 1, 1, 2, 2, 2, 2, 3, 3, 0, 0, 0]

        # Fill the max_right array with the maximum height to the right of each element.
        for i in range(num_elements - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])
              #    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]
        #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1]
        #     [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1]
        #     [1, 1, 1, 1, 1, 1, 1, 3, 2, 2, 2, 1]
        #     [1, 1, 1, 1, 1, 1, 3, 3, 2, 2, 2, 1]
        #     [1, 1, 1, 1, 1, 3, 3, 3, 2, 2, 2, 1]
        #     [1, 1, 1, 1, 3, 3, 3, 3, 2, 2, 2, 1]
        #     [1, 1, 1, 3, 3, 3, 3, 3, 2, 2, 2, 1]
        #     [1, 1, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
        #     [1, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
        #     [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]

        # Calculate the total amount of trapped water using the height difference
        # between the minimum of max_left and max_right for each element and the height at that element.
        trapped_water = sum(min(max_left[i], max_right[i]) - height[i] for i in range(num_elements))

        # Return the total amount of trapped water.
        return trapped_water