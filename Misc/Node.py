def calculate_conversion_rate(conversion_data, source_currency, target_currency):
    conversion_rates = {}
    visited_set={}

    for data in conversion_data:
        source, target, rate = data.split(', ')
        conversion_rates[(source, target)] = float(rate)

    memo = {}

    def dfs(current_currency):
        if current_currency == target_currency:
            return 1.0

        if current_currency in memo:
            return memo[current_currency]

        result = 0.0
        for currency in conversion_rates:
            if currency[0] == current_currency:
                result = max(result, conversion_rates[currency] * dfs(currency[1]))

        memo[current_currency] = result
        return result if result else -1.0

    result = dfs(source_currency)
    return round(result, 2)

# Input data
conversion_data = ["USD, GBP, 0.7", "USD, JPY, 109", "GBP, JPY, 155", "CAD, CNY, 5.27", "CAD, KRW, 921", "CAD, JPY, 2"]
source_currency = "USD"
target_currency = "CNY"

# conversion_data = ["USD, CAD, 1.3", "USD, GBP, 0.71", "USD, JPY, 109", "GBP, JPY, 155"]
# source_currency = "USD"
# target_currency = "JPY"

# Calculate conversion rate
conversion_rate = calculate_conversion_rate(conversion_data, source_currency, target_currency)
print(conversion_rate)


