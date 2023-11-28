import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...

def max_profit(prices, k):
    n = len(prices)
    dp = [[0]* (k+1) for _ in range(n)]
    
    for i in range(1, n):
        for j in range(1,k+1):
            max_profit = 0
            
            for x in range(i):
                max_profit = max(max_profit, prices[i] - prices[x] + dp[x][j-1])
            
            dp[i][j] = max(dp[i-1][j], max_profit)
                
            
    total_profit = dp[n-1][k]
    i, j= n-1, k
    trades = 0
    
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            trades+=1 
            
            while i > 0 and dp[i][j] == prices[i] - prices[i-1] + dp[i-1][j-1]:
                i-=1
            j-=1
        else:
            i-=1
            
    return total_profit, trades
          
                

for line in sys.stdin:
    prices, k = line.split(';')
    prices = [int(x) for x in prices.split(',')]
    k = int(k)
    
    profit, trades = max_profit(prices, k)
    print(f"{profit},{trades}")
    
                       
                   
        
