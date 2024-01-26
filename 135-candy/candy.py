class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = 0
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        
        # Left relative array
        for i in range(1, n):
            # If current index rating > previous; give extra candies
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            # print(left)
        
        # Right relative array
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            # print(right)
        
        # Merge both the sides
        for i in range(n):
            candies += max(left[i], right[i])
        
        return candies