class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # given the citations array [3,0,6,1,5], we can sort it to obtain [6,5,3,1,0].
        citations.sort(reverse=True) # Sort the array in non-increasing order
        n = len(citations)
        h = 0
        
        # Iterate through the sorted array and compare each citation count to the number of papers that have at least that many citations
        for i in range(n):
            if citations[i] >= i+1: # If the citation count is greater than or equal to the number of papers with at least that many citations, we have found the h-index
                h = i+1
        
        return h