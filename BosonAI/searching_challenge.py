'''
-----------------------------------------------------------------------
File: searching_challenge.py
Creation Time: Jun 16th 2024, 3:21 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''
"""
Searching Challenge

Have the function SearchingChallenge (str) take str which will be a string and return the longest pattern within the string. A pattern for this challenge will be defined as: if at least 2 or more adjacent characters within the string repeat at least twice. So for example "aabecaa" contains the pattern aa, on the other hand "abbbaac" doesn't contain any pattern. Your program should return yes/no pattern/null. So if str were "aabejiabkfabed" the output should be yes abe. If str were "123224" the output should return no null. The string may either contain all characters (a through z only), integers, or both. But the parameter will always be a string type. The maximum length for the string being passed in will be 20 characters. If a string for example is "aa2bbbaacbbb" the pattern is "bbb" and not "aa". You must always return the longest pattern possible.

Examples

Input: "da2kr32a2"

Output: yes a2

Input: "sskfssbbb9bbb"

Output: yes bbb

"""

def SearchingChallenge(s):
    max_pattern = ""
    max_length = 0

    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            pattern = s[i:j]
            if s.count(pattern) > 1:
                if len(pattern) > max_length:
                    max_pattern = pattern
                    max_length = len(pattern)

    if max_pattern:
        return f"yes {max_pattern}"
    else:
        return "null"

# Test cases
print(SearchingChallenge("da2kr32a2")) # Output: yes a2
print(SearchingChallenge("sskfssbbb9bbb")) # Output: yes bbb
print(SearchingChallenge("aajebiakbfabed")) # Output: yes ae
print(SearchingChallenge("123224")) # Output: null