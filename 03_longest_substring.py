class Solution():
    def lengthOfLongestSubstring(self, s):
        """Counting the substrings

        Args:
            Longest Substring without repeating characters
            Given a string "s", find the length of the longest substring without repeating characters

            Example 1:
            Input: s = 'abcabcbb'
            Output: 3
            Explanation: The answer is "abc", with the length of 3.

            Example 2:
            Input: s = "bbbbb"
            Output: 1
            Explanation: The answer is "b", with the length of 1.

            Example 3:
            Input: s = "pwwkew"
            Output: 3
            Explanation: The answer is "wke", with the length of 3.
            Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

        Returns:
            max_length: it'll return the count of the occurrence on the string
        """
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):                         # Se não tiver no set, vai adicionar e não entra no while
            while s[right] in char_set:                     # Quando encontrar no set ele remove e adiciona +1 no left
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])                          # Adiciona a substring no set
            max_length = max(max_length, right - left + 1)  # vai retornar o maior número do max_length

        return max_length

    # 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    # d | a | b | c | a | b | c | b | b | d

s = Solution()

print(s.lengthOfLongestSubstring('abcabcbb')) # Comprimento: 3
print(s.lengthOfLongestSubstring('bbbbb'))    # Comprimento: 1
print(s.lengthOfLongestSubstring('wwkew'))   # Comprimento: 3