from linked_deque import LinkedDeque
# from stock_purchase import StockPurchase

class LedgerEntry:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.deque = LinkedDeque()
        # makes a new entry using the given stock symbol

    def add_purchase(self, new_purchase):
        self.deque.add_to_back(new_purchase)
        # new_purchase will be a stock_purchase ADT
        # add nodes to the back of the deque

    def remove_purchase(self):
        self.deque.remove_front()
        # Removes the front entry on the LedgerEntry its called for


    def equals(self, other):
        if self==other:return True  # Equals : True
        else:return False           # Doesn't equal : False
        
    def display_entry(self):
        # using a dictionary cause I couldn't think of an easier way to map
        # prices to number purchased while counting
        price_counts = {}
        current = self.deque.head
        while current is not None:
            SP = current.get_data()
            price = SP.get_cost()
            if price in price_counts:
                price_counts[price] += 1
            else:
                price_counts[price] = 1
            current = current.get_next_node()
        result = f"{self.stock_symbol}: "
        result += ", ".join([f"{price} ({count} shares)" for price, count in price_counts.items()])
        return result
        # counts how many stonks at each price
        # outputs the counts with their respective prices

# extra methods
    def get_deque(self): return self.deque
    def get_symbol(self): return self.stock_symbol
    def get_deque_size(self): return self.deque.size()