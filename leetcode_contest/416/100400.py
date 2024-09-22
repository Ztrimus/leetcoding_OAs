'''
-----------------------------------------------------------------------
File: 416/100400.py
Creation Time: Sep 21st 2024, 7:54 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

"""
100400. Report Spam Message
User Accepted:12910
User Tried:15342
Total Accepted:14723
Total Submissions:30414
Difficulty:Medium
You are given an array of strings message and an array of strings bannedWords.

An array of words is considered spam if there are at least two words in it that exactly match any word in bannedWords.

Return true if the array message is spam, and false otherwise.

 

Example 1:

Input: message = ["hello","world","leetcode"], bannedWords = ["world","hello"]

Output: true

Explanation:

The words "hello" and "world" from the message array both appear in the bannedWords array.

Example 2:

Input: message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]

Output: false

Explanation:

Only one word from the message array ("programming") appears in the bannedWords array.

 

Constraints:

1 <= message.length, bannedWords.length <= 105
1 <= message[i].length, bannedWords[i].length <= 15
message[i] and bannedWords[i] consist only of lowercase English letters.
"""

from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned_set = set(bannedWords)
        count = 0
        for word in message:
            if word in banned_set:
                count += 1
            if count > 1:
                return True
        return False

obj = Solution()

for testcase in [
    [["l","i","l","i","l"], ["d","a","i","v","a"], True],
    [["hello","world","leetcode"], ["world","hello"], True],
    [["hello","programming","fun"], ["world","programming","leetcode"], False],
]:
    print(f"meg: {testcase[0]}, banned: {testcase[1]}, expected: {testcase[2]} => {obj.reportSpam(testcase[0], testcase[1])}")