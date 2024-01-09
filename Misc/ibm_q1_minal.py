'''
-----------------------------------------------------------------------
File: ibm_q1_minal.py
Creation Time: Nov 1st 2023 10:37 pm
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
'''

def getQueryResults(N, queries):
    def generateGoodArray(N):
        goodArray = []
        k = 0
        while N > 0:
            if N % 2 == 1:
                goodArray.append(2**k)
            N //= 2
            k += 1
        return sorted(goodArray)

    answers = []
    goodArray = generateGoodArray(N)
    
    for query in queries:
        l, r, m = query
        product = 1
        for i in range(l - 1, r):
            product *= goodArray[i]
        answers.append(product % m)

    return answers

# Example usage:
N = 12
queries = [[1,2,84], [2,2,3]]
results = getQueryResults(N, queries)
print(results)  # Output: [16, 1]