class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

     

 
	p1, p2, write_index = m-1, n-1, m + n - 1

	while p2 >= 0:
		if p1 >= 0 and nums1[p1] > nums2[p2]:
			nums1[write_index] = nums1[p1]
			p1 -= 1
		else:
			nums1[write_index] = nums2[p2]
			p2 -= 1

		write_index -= 1