import os 
from collections import defaultdict

def getNetProfit (events):
    portfolio = defaultdict(int)
    net_profit = 0
    result = []

    for event in events:
        division = event.split()
        category, stock, value = None, None, None
        category =  division[0] if division[0] else None
        if len(division) >1:
            stock = division[1]
            if len(division) >2:
                value =  division[2]
                
        if category == "BUY":
            portfolio[stock] += int(value)

        elif category == "SELL":
            portfolio[stock] -= int(value)

        elif category == "CHANGE":
            change = portfolio[stock]*int(value)
            net_profit += change

        elif category == "QUERY":
            result.append(net_profit)

    return result

if __name__ == '__main__':
    events_count = int(input().strip())
    events = []
    for _ in range (events_count): 
        events_item = input() 
        events.append (events_item)
    result = getNetProfit (events)
    
    print('\n'.join(map (str, result))) 
    print('\n')