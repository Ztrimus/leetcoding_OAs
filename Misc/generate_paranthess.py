'''
-----------------------------------------------------------------------
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
File: generate_paranthess.py
Creation Time: Oct 27th 2023 11:37 am
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
'''
from typing import List

def generateParenthesis(n: int) -> List[str]:
    s = ""
    res = []

    def backtrack(open, close, s, d):
        print("\t"*d,f"enter {d}")
        if open == close == n:
            res.append(s)
            return

        if open < n:
            s += "("
            backtrack(open+1, close, s, d+1)
            s = s[:-1]
        
        if close < open:
            s += ")"
            backtrack(open, close+1, s, d+1)
            s = s[:-1]
        
        print("\t"*d,f"exit {d}")
    
    backtrack(0,0,s,0)
    return res

print(generateParenthesis(3))

# def dailyTemperatures(temperatures: List[int]) -> List[int]:
#     res = []
#     len_temp = len(temperatures)
#     for i in range(len_temp):
#         d = 1
#         if i+d >= len_temp:
#                 d = 0
#         else:
#             while temperatures[i] > temperatures[i+d]:
#                 d+=1
#                 if i+d >= len_temp:
#                     d = 0
#                     break
#         res.append(d)
#     return res

# print(dailyTemperatures([73,74,75,71,69,72,76,73]))
# # print(dailyTemperatures([30,40,50,60]))