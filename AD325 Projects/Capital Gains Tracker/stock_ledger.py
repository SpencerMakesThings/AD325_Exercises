from stock_purchase import StockPurchase # when a buy command is used on the ledger
from ledger_entry import LedgerEntry
# the ledger will execute 

class StockLedger:
    def __init__(self):
        self.ledger = [] # a list for our ledger entries
        # list holds ledger_entries which have a name (stock_symbol) and a deque


    def buy(self, stock_symbol, shares_bought, price_per_share):
        if not self.contains(stock_symbol):     # if there's no entry by that name
            new_entry = LedgerEntry(stock_symbol)   # make a new ledger entry for it
            self.ledger.append(new_entry)           # append it to the list
        # then a second section where we append our stonks to the appropriate list
        SP = StockPurchase(stock_symbol,price_per_share)
        for i in self.ledger:
            if (i.get_symbol() == stock_symbol):
                stonk = i # grab the ledger_entry object we're looking for
                break
        for j in range(shares_bought):  # makes shares_bought number purchases
            stonk.add_purchase(SP)      
        # if there's no ledger_entry, make a new one named stock_symbol
        # if there's LE named stock_symbol, add shares_bought nodes holding price_per_share

    def sell(self, stock_symbol, shares_sold, price_per_share):
        if self.contains(stock_symbol):
            entry = self.get_entry(stock_symbol)
            if (entry.get_deque_size() >= shares_sold): # if there's at least shares_sold number of nodes
                # ledger_entry remove() command
                # remove shares_sold nodes from the end of the deque
                for i in range(shares_sold):
                    entry.remove_purchase() # execute remove shares_sold times
            else:
                print('Error: shares_owned < shares_sold')
        else: print('Error: That stock is not on the ledger')
        # if there's an LE named stock_symbol, and there are at least share_sold nodes
        # sell them


    def display_ledger(self):
        for i in self.ledger:
            print(i.display_entry())
        # roll through the whole ledger
        # call display_entry(LedgerEntry) on each entry


    def contains(self, stock_symbol):   # name the first half of the tuple "stonk"
        for stonk in self.ledger:    # roll through the list comparing stonk to symbol
            if (stonk.get_symbol() == stock_symbol): # if the stonk has the name we're looking for
                return True             # return True
        return False                # otherwise return False
    
    def get_entry(self, stock_symbol):  # 
        for entry in self.ledger:           # Search the ledger til we find the stock_symbol
            if entry.get_symbol() == stock_symbol:    # entry[0] is the "stock_symbol" part of the tuple
                return entry    # return the whole ledger entry for that stock
        else: return None       # return None if we don't find it


    # Some extra methods for doing other stuff


    def get_deque_size(self, stock_symbol):
        entry = self.get_entry(stock_symbol)
        deque = entry.get_deque() # get the LE we're looking for
        if deque: return deque.size() # use the size() method from LD to check deque length
        return 0    # if it's not there return 0
