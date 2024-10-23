class LedgerEntry:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        # makes a new entry using the given stock symbol

    def add_purchase(self, new_purchase):
        pass
        # add

    def remove_purchase(self):
        pass
        # Removes the front entry on the provided LedgerEntry

    def equals(self, other):
        if self==other:
            return True
        else:
            return False
        
    def display_entry(self):
        pass
        # counts how many stonks at each price
        # outputs the counts with their respective prices
