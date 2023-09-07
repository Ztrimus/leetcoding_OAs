import math


buy_orders = [
  (100, 1850),
  (200, 1850.25),
  (300, 1850.50),
]

sell_orders = [
  (100, 1849.75),
  (200, 1849.50),
  (300, 1849.25),
]

trade_risk = [
  (15, 0.25),
  (1, 0.25),
]

buy_stack = []
for qty, price in buy_orders[::-1]: buy_stack.extend([price]*qty)

sell_stack = []
for qty, price in sell_orders[::-1]: sell_stack.extend([price]*qty)

def get_afp(risk_to_offset, stack):
  tmp = [stack.pop() for _ in range(abs(risk_to_offset))]
  return sum(tmp)/len(tmp)


cf = 0
for qty, rpu in trade_risk:
  tot_risk = (qty * rpu) + cf
  risk_to_offset = math.floor(tot_risk)  # if -0.9 => math.floor will give -1, whcih we don't want. We want 0
  cf = tot_risk - risk_to_offset

  risk_to_offset = -risk_to_offset
  if risk_to_offset > 0: afp = get_afp(risk_to_offset, buy_stack)
  elif risk_to_offset < 0: afp = get_afp(risk_to_offset, sell_stack)
  else: afp = 0 # format

  print(f'{risk_to_offset} | {afp:0.2f}')
  
