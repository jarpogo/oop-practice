class Bill:
    """
    Object that contains data about a bill, such as
    the total amount and period of a bill.
    """
    
    def __init__(self, amount, period) -> None:
        self.amount = amount
        self.period = period
