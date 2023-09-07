import sys

buy = [[100, 1850.0], [200, 1850.25], [300, 1850.5]]
sell = [[100, 1849.75], [200, 1849.50], [300, 1849.25]]

sign = [[15, 0.25], [1, 0.25]]
# sign = [[10, 0.20], [15, -0.20], [-40, 0.50]]

def naiveHedgingProblem(buy, sell, sign):
    riskOperation = []
    remaining = 0
    for i in sign:
        risk = i[0]*i[1]+remaining
        riskOperation.append(int(risk)*-1)
        remaining = risk - int(risk)
    
    buyIndex=0
    sellIndex=0
    for i in riskOperation:
        if i > 0:
            if buy[buyIndex][0] <= 0:
                buyIndex+=1
            buy[buyIndex][0] -= i
            print(f"{i} {buy[buyIndex][1]}")
   

        elif i < 0:
            if sell[sellIndex][0] <= 0:
                sellIndex+=1
            sell[sellIndex][0] -= i
            print(f"{i} {sell[sellIndex][1]}")

naiveHedgingProblem(buy, sell, sign)

# flag = 0
# buy = [[0,0] for i in range(3)]
# sell = [[0,0] for i in range(3)]
# for line in sys.stdin:
#     if flag == 0:
#         for i,j in enumerate(line.split()):
#             buy[i//2][i%2] = float(j) if i%2 == 1 else int(j)
#     elif flag==1:
#         for i,j in enumerate(line.split()):
#             sell[i//2][i%2] = float(j) if i%2 == 1 else int(j)
#     else:
#         pass

#     flag+=1

# print(buy)



# dd = '100 1850.00 200 1850.25 300 1850.50'