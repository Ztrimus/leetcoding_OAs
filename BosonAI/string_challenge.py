'''
-----------------------------------------------------------------------
File: string_challenge.py
Creation Time: Jun 16th 2024, 3:30 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

"""
String Challenge

Have the function StringChallenge (str) take the str parameter being passed and return a compressed version of the string using the Run-length encoding algorithm. This algorithm works by taking the occurrence of each repeating character and outputting that number along with a single character of the repeating sequence. For example: "wwwggopp" would return 3w2g102p. The string will not contain any numbers, punctuation, or symbols.

Once your function is working, take the final output string and concatenate it with your ChallengeToken, and then replace every third character with an X.

Your ChallengeToken: vga1slxwrd35

Examples

Input: "aabbcde"

Output: 2a2b1c1d1e

Final Output: 2aXb1X1dXevXa1XlxXrdX5

Input: "wwwbbbw"

Output: 3w3b1w

Final Output: 3wXb1XvgX1sXxwXd3X
"""

def StringChallenge(s):
    # Step 1: Compress the string using Run-length encoding
    compressed = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        compressed.append(f"{count}{s[i]}")
        i += 1
    compressed_str = ''.join(compressed)

    # Step 2: Concatenate the compressed string with the ChallengeToken
    challenge_token = "vga1sbkwrd35"
    final_str = compressed_str + challenge_token

    # Step 3: Replace every third character with an 'X'
    result = []
    for i, char in enumerate(final_str):
        if (i + 1) % 3 == 0:
            result.append('X')
        else:
            result.append(char)
    final_output = ''.join(result)

    return final_output

# Test cases
print(StringChallenge("aabbccde"))  # Example input from the challenge
print(StringChallenge("wwwbbbww"))  # Example input from the challenge