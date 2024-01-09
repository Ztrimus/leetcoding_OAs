import sys

class Bundle:
    def __init__(self, name, price, components):
        self.name = name
        self.price = price
        self.components = components

class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def PrintTrade(name, bundleOrStock, price):
    p="{:.2f)".format(price)
    print("{} E {} {}".format(name, bundleOrStock, p))

def PrintNoTrade(name):
    print("{} P".format(name))

class MarketWatchPortfolio:
    def __init__(self, bundles, stocks):
        self.bundles = bundles
        self.stocks = stocks
    
    def ExecuteTrades (self):
        # TODO (candidate): fill out
        pass

def ParseInputs():
    bundles= list()
    stocks= dict()
    num_stocks = -1
    num_bundles = -1
    for line in sys.stdin:
        parsed = line.strip().split(' ')
        if num_bundles -1 and num_stocks -1:
            num_bundles = int(parsed[0])
            num_stocks = int(parsed[1])
            continue
        if num_bundles > 0:
            components = list()
            for i in range(3, len(parsed)-1, 2):
                components.append((int(parsed[i+1]), parsed[i]))
            bundles.append(Bundle (parsed[0], float (parsed[1]), components))
            num_bundles -= 1
            continue
        s = Stock(parsed[0], float (parsed[1]))
        stocks[parsed[0]] = s
    return MarketWatchPortfolio (bundles, stocks)

def main():
    portfolio = ParseInputs() 
    portfolio.ExecuteTrades()

if __name__ == '__main__':
    main()