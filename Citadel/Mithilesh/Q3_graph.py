'''
-----------------------------------------------------------------------
File: Mithilesh/Q3_graph.py
Creation Time: Jul 21st 2024, 6:43 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

from collections import defaultdict

def getMaxList(n, frdshp):
    mtx = defaultdict(set)
    res = [-1]*n

    for u,v in frdshp:
        mtx[u].add(v)
        mtx[v].add(u)
    
    mtx_1 = defaultdict(set)
    for i in mtx:
        for j in mtx[i]:
            mtx_1[i].add(j)
            for k in mtx[j]:
                mtx_1[i].add(k)


    print(mtx)
    pass

print(getMaxList(5, [[0,1],[0,2],[1,3],[2,3],[3,4]]))