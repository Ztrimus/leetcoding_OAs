'''
-----------------------------------------------------------------------
File: TP/random_note.py
Creation Time: Jul 20th 2024, 8:19 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

def canConstruct(ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine:
                return False
            magazine = magazine.replace(i, '', 1)
        return True

print(canConstruct("aa", "ab")) # Output: False