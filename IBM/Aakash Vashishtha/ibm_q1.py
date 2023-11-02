'''
-----------------------------------------------------------------------
File: ibm_q1.py
Creation Time: Nov 2nd 2023 12:06 am
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
'''

def getQueryResults(n, queries):
    def gArray(n):
        goodArray = []
        k = 0
        while n > 0:
            if n % 2 == 1:
                goodArray.append(2**k)
            n//=2
            k+=1
        return sorted(goodArray)
        
    answers = []
    goodArray = gArray(n)
    for query in queries:
        l,r,m = query
        product = 1
        for i in range(l-1, r):
            product *= goodArray[i]
        answers.append(product % m)
    return answers