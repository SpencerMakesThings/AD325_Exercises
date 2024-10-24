from linked_deque import LinkedDeque, DLNode
from stock_purchase import StockPurchase

class LedgerEntry:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.deque = LinkedDeque()
        # makes a new entry using the given stock symbol

    def add_purchase(self, new_purchase = StockPurchase):
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
        pass
        # counts how many stonks at each price
        # outputs the counts with their respective prices

# extra methods
    def get_deque(self): return self.deque