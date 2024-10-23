class StockLedger:
    def __init__(self):
        pass
    def buy(self, stock_symbol, shares_bought, price_per_share):
        pass
        # creates shares_bought new DLNodes holding price_per_share
        # adds those nodes to the end of the LedgerEntry named stock_symbol
    def sell(self, stock_symbol, shares_sold, price_per_share):
        pass
    def display_ledger(self):
        pass
        # runs display_entry on each LedgerEntry in the deque
            # takes each LE deque using display()

    def contains(self, stock_symbol):
        pass
        # checks if there's an LE named +stock_symbol
    def get_entry(self, stock_symbol):
        if self.contains(stock_symbol):
            return 
        pass
        # returns a LE named stock_symbol (if it exists)