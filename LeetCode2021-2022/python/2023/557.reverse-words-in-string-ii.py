class Solution:
    def reverseWords(self, s: str) -> str:
        """reverse words in s while perserving the whiltespace
        Strategy 1: Brute force
        Runtime: O(n)
        Space: O(n)

        Args:
            s (str): list of words with white space in between  

        Returns:
            str: reversed words with white space
        """
        words = s.split(" ")
        reverse = []
        for word in words:
            reverse.append(word[::-1])
        return " ".join(reverse)
