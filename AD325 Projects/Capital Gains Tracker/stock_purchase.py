class StockPurchase:
    def __init__(self, stock_symbol, cost_per_share):
        self.stock_symbol = stock_symbol    # Stock name
        self.cost_per_share = cost_per_share# Price to store on DLNode
        # make a new DLNode with cost_per_share as it's data_portion
        # add it to the end of the LedgerEntry list named stock_symbol

    # New methods
    def get_cost(self): return self.cost_per_share
    def get_symbol(self): return self.stock_symbol
    # this should all work but I'm putting comments on shit to see if it registers that these files have changed