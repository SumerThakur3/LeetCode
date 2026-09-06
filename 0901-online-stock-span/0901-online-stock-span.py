class StockSpanner:

    def __init__(self):

        self.stack=[]  #stack stores (price,span)
        
    def next(self, price: int) -> int:
        span=1
        #stack[-1][0] gives us top stack price
        while self.stack and self.stack[-1][0]<=price: 
            #stack[-1][1] gives us top stack span
            span+=self.stack[-1][1]
            #remove the previous price and span
            self.stack.pop()
        #adds todays price and span
        self.stack.append((price,span))

        return span    


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)