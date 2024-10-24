from stock_purchase import StockPurchase # when a buy command is used on the ledger
from ledger_entry import LedgerEntry
# the ledger will execute 

class StockLedger:
    def __init__(self):
        self.ledger = [] # a list for our ledger entries
        # list entries have a name (stock_symbol) and a deque
        # we can store these as tuples
    def buy(self, stock_symbol, shares_bought, price_per_share):
        if not self.contains(stock_symbol): # if there's no entry by that name
            #create a new ledger_entry
            entry = LedgerEntry
            self.ledger.append(entry)
        pass
        # if there's no ledger_entry, make a new one named stock_symbol
        # if there's LE named stock_symbol, add shares_bought nodes holding price_per_share
    def sell(self, stock_symbol, shares_sold, price_per_share):
        if self.contains(stock_symbol):
            entry = self.get_entry(stock_symbol)
            if (entry.get_deque_size() >= shares_sold): # if there's at least shares_sold number of nodes
                # ledger_entry remove() command
                # remove shares_sold nodes from the end of the deque
                pass
            else:
                print('Error: shares_owned < shares_sold')
        else: print('Error: That stock is not on the ledger')
        # if there's an LE named stock_symbol, and there are at least share_sold nodes
        # sell them
            # if we were going for extra credit, we might add in here some
            # math to compute profit made on each share sold and return it
    def display_ledger(self):
        pass
        # roll through the whole ledger
        # call display_entry(LedgerEntry) on each entry

    def contains(self, stock_symbol):   # name the first half of the tuple "stonk"
        for stonk, _ in self.ledger:    # roll through the list comparing stonk to symbol
            if (stonk == stock_symbol): # if the stonk has the name we're looking for
                return True             # return True
        return False                # otherwise return False
    
    def get_entry(self, stock_symbol):  # 
        for entry in self.ledger:           # Search the ledger til we find the stock_symbol
            if entry[0] == stock_symbol:    # entry[0] is the "stock_symbol" part of the tuple
                return entry    # return the whole ledger entry for that stock
        else: return None       # return None if we don't find it


    # Some extra methods for doing other stuff


    def get_deque_size(self, stock_symbol):
        entry = self.get_entry(stock_symbol)
        deque = entry.get_deque() # get the LE we're looking for
        if deque: return deque.size() # use the size() method from LD to check deque length
        return 0    # if it's not there return 0
