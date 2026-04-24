class StockSpanner:

    def __init__(self):
        self.stack = []
        # self.count = 0

    def next(self, price: int) -> int:
        count = 1

        while self.stack and self.stack[-1][1] <= price:
            count += self.stack.pop()[0]
            # self.stack.pop()

        self.stack.append((count, price))
        
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)