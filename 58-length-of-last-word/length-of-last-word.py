class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 
        
        for i in range(len(s) - 1, -1, -1):
            # a letter is found so count
            if s[i] != ' ':
                count += 1
            else:
                # it's a white space instead
                # Did we already start to count a word?
                # Yes, so we found the last word
                if count > 0:
                    return count
        return count