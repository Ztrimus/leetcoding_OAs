## Trading Platform

A quantitative trading firm seeks to create a tool for querying the net profit/loss of the firm at any given time. The tool processes a list of events, each of which can be classified into one of four categories:

1. BUY stock quantity. Signifies the purchase of <quantity> shares of stock <stock> at the
market price. 
2. SELL stock quantity. Indicates the sale of <quantity> shares of stock <stock> at the market price.
3. CHANGE stock price: Signifies a change in the market price of <stock> by <price> amount which can be either positive or negative.
4. QUERY: Represents a query for the net profit/loss from the start of trading to the present.


The tool should return a list of numbers corresponding to each QUERY event.

#### Example
For instance, given the list of events ["BUY googl 20", "BUY aapl 50", "CHANGE googl 6", "QUERY", "SELL aapl 10", "CHANGE aapl -2", "QUERY"].
| Events | Portfolio | Profit so far |
| BUY googl 20 | googl 20 | 0 | 
| BUY aapl 50 |  googl 20, aapl 50 |  0 |
| CHANGE googl 6 | googl 20,  aapl 50 |  120 |
| QUERY | | 120 |
| SELL aapl 10 | googl 20,  aapl 40 | 120 |

Hence the answer should be [120, 40].

#### Function Description
Complete the function getNetProfit in the editor below.

    getNetProfit has the following parameter: string events[n]: the events to process

Returns
    int[]; the answers to the "QUERY" events

Constraints
• 1 ≤n≤ 10^5
• | events[i] | ≤21
    • For query, SELL <stock> <quantity>, it is guaranteed that there are enough shares owned. 
    • 1 ≤ quantity<103
• The absolute value of a change in the price of any stock at any event will not exceed 103.

#### Input Format For Custom Testing 
The first line contains an integer, n, the number of elements in events.
Each line i of the n subsequent lines (where 0 ≤ i<n) contains a string that represents events[i].

#### Sample Case 0

Sample Input For Custom Testing
STDIN           FUNCTION
------       -------------
2 ->           n = 5
BUY hackr 2 -> events = ["BUY hackr 2", "QUERY"]
QUERY

Sample Output
Explanation
The firm purchased 2 stocks of hackr, then have a "QUERY" event. Since there is no change in stock price, there is 0 profit so far.


#### Sample Case 1
Sample Input For Custom Testing
STDIN           FUNCTION
------       -------------
6 ->                n=5
BUY stock2 2 -> events = ["BUY stock2 2", "BUY stock1 4", "CHANGE stock2 -8", "SELL stock1 2", "BUY stock3 3", "QUERY"]
BUY stockl 4
CHANGE stock2 -8
SELL stock1 2
BUY stock3 3
QUERY

Sample Output
-16

Explanation
The price of 2 shares of stock2 decreased by 8.


```python
Coding Template Below

def getNetProfit (events):
    #Write your code here
    pass


if name == 'main':
    fptr = open (os.environ ['OUTPUTPATH'], 'w')
    eventscount = int(input().strip())
    events = []
    for _ in range (eventscount): 
        eventsitem = input() 
        events.append (events_item)
    result = getNetProfit (events)


fptr.write('\n'.join(map (str, result))) 
fptr.write('\n')

fptr.close()
```


# sample 1
7
BUY googl 20
BUY aapl 50
CHANGE googl 6
QUERY
SELL aapl 10
CHANGE aapl -2
QUERY

# sample 2
2
BUY hackr 2
QUERY

# sample 3
6 
BUY stock2 2
BUY stock1 4
CHANGE stock2 -8
SELL stock1 2
BUY stock3 3
QUERY

# sample 3
6 
BUY stock2 2
BUY stock1 4
CHANGE stock2 -8
SELL stock2 1
BUY stock3 3
QUERY