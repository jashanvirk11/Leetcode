class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the input string on spaces to get a list of words
        words = s.split()
       
        # Reverse the list of words
        reversed_words = reversed(words)
      
        # Join the reversed list of words back into a string with spaces
        reversed_sentence = ' '.join(reversed_words)
      
        # Return the reversed sentence
        return reversed_sentence