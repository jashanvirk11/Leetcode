class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
    
        temp = x
        reverse=0

        while x>0:
            last_digit = x%10
            reverse = last_digit+(reverse*10)
            x = x/10

        if temp == reverse:
           return True
        else:
           return False
    