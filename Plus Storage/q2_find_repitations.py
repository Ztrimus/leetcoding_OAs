'''
-----------------------------------------------------------------------
File: q2_repitation.py
Creation Time: Jan 27th 2024, 9:48 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

def findRepitationCount(short_s, long_s):
    result = 0
    len_short_s = len(short_s)
    
    i = 0
    while i <= len(long_s)-len_short_s:
        count = 0
        while long_s[i:i+len_short_s] == short_s:
            count += 1
            i+=len_short_s
        
        result = max(result, count)
        i+=1
    
    return result
        

    pass

print(findRepitationCount("AB", "ABCABCABAB"))

print(findRepitationCount("AB", "ABBAC"))

