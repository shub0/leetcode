#! /usr/bin/python

'''
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        size = len(s)
        sub_set = set()
        start = 0
        end = 0
        substring = ''
        while end < size:
            char = s[end]
            if char not in sub_set:
                sub_set.add(char)
                end += 1
                continue
            if end - start > len(substring):
                substring = s[start:end]
            while start < end:
                cur_char = s[start]
                sub_set.remove(cur_char)
                start += 1
                if cur_char == char:
                    break
        if end - start > len(substring):
            substring = s[start:end]
        return len(substring)

if __name__ == '__main__':
    solution = Solution()
    print solution.lengthOfLongestSubstring('ohomm')
    print solution.lengthOfLongestSubstring('abcdc')
    print solution.lengthOfLongestSubstring('bbb')
