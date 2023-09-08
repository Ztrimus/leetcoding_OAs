from dataclasses import dataclass

@dataclass
class Dividend:
    amount: int
    days: int


class FuturePricingEngine:
    def __init__(self, stock_price: int, dividends: list[Dividend]):
        self.stock_price = stock_price
        self.dividends = dividends
        pass  # Enter your code here

    def update_dividend(self, dividend_id: int, updated_dividend: Dividend):
        self.dividends[dividend_id-1] = updated_dividend
        pass  # Enter your code here

    def calculate_future_price(self, days_to_future: int) -> int:
        price = self.stock_price
        for dividend in self.dividends:
            if dividend.days <= days_to_future:
                price -= dividend.amount
        return price
        pass  # Enter your code here

# TAIL
if __name__ == "__main__":
    import sys

    read_line = lambda: sys.stdin.readline().split()

    first_line = read_line()
    stock_price = int(first_line[0])
    num_dividends = int(first_line[1])
    num_queries = int(first_line[2])

    dividends: list[Dividend] = []

    for _ in range(num_dividends):
        line = read_line()
        amount = int(line[0])
        days = int(line[1])
        div = Dividend(amount, days)
        dividends.append(div)

    engine = FuturePricingEngine(stock_price, dividends)

    for _ in range(num_queries):
        line = read_line()
        if line[0] == 'DIVIDEND_UPDATE':
            dividend_id = int(line[1])
            amount = int(line[2])
            days = int(line[3])
            updated_dividend = Dividend(amount, days)
            engine.update_dividend(dividend_id, updated_dividend)
        elif line[0] == 'PRICE':
            days = int(line[1])
            future_price = engine.calculate_future_price(days)
            print(future_price)
        else:
            raise Exception('invalid input')