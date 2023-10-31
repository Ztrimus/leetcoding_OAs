'''
-----------------------------------------------------------------------
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
Creation Time: Oct 30th 2023 10:59 pm
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
File: q3_mentions.py
-----------------------------------------------------------------------
'''
import re

def find_mentions(text):
    pattern = r'@id(\d+)(?:,\s*id(\d+))*'
    mentions = re.findall(pattern, text)
    flattened_mentions = set(['id'+mention for group in mentions for mention in group if mention])
    return flattened_mentions

def solution(members, messages):
    res = {member: 0 for member in members}
    for msg in messages:
        for mention in find_mentions(msg):
            if mention in res:
                res[mention] += 1
    res = sorted(res.items(), key=lambda x: (x[0]))
    res = sorted(res, key=lambda x: (x[1]), reverse=True)
    return [f"{i[0]}={i[1]}" for i in res]

# members = ["id123", "id234", "id7", "id321"]

# messages = [
#     "Hey @id123,id321 review this PR please! @id123 what do you think", 
#     "Hey @id7 nice appro@ch! Great job! @id800 what do you think?", 
#     "@id123,id321 thx!"
# ]

members = ["id962", "id650", "id824"]
messages = [
    "id824 @id824,id560,id726 Nsdej. 7pok @id248,id942 @id593 1uh?P2W G@PNq @id475 @id650,1d824,1d73 ZoPkHh! @id711,id650,id497,id448 @id98 T9a0vF ? gPPLgs UkeN@R1 id962",
    "haooRio XdVJNZT K7UO R.061 Sbo15qN CR2usU G9TkoQx !VgH id959 macxz qRR. ?vzety bjvcG", "@id815, id877 @id962 @id872 @id542,id962 1d4f @id964, id180 @id680,id530 As?sOT6 DtGOS I!RFO",
    "@id732,id705 1Mp!J1 W9KH6 vdi3uwq Evz6j ruDxV ERPIK QFYWW B64rUOV yb@31 id475,id540 SFFRZ TSUL rK8CF gfqt o!uE4I zar2!3B 3SJuwvr Y3SF Lotcf2x id425",
    "@id590,id957,id869,id650,id824,id176,id936 @id824,id304 @id283,id931,id277,id65,id468,id962,id213,id962,id356 @id4,id834"
    ]


print(solution(members, messages))