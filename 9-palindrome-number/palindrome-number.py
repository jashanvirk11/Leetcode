class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
    
        temp = x
        sum=0

        while x>0:
            rem = x%10
            sum = rem+(sum*10)
            x = x/10

        if temp == sum:
           return True
        else:
           return False
    