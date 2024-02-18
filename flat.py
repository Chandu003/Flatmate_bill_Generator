class Bill:
    """
    Object that contains about a bill, such as total amount and
    period of that bill.
    """
    def __init__(self,amt, period):
        self.amt = amt
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flast and pays a
    share of the bill.
    """

    def __init__(self,name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self,bill,flatmate2):
        weight = self.days_in_house/ (self.days_in_house + flatmate2.days_in_house)
        return weight * bill.amt