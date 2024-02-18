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

    def pays(self,bill):
        return bill.amt / 2


class PDFReport:
    """
    Create pdf file that contains data about
    the flatmates details and bill details.
    """

    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatemate1,flatmate2,bill):
        pass

bill = Bill(amt=120,period="March 2021")
john = Flatmate(name="john",days_in_house=20)
marry = Flatmate(name="marry",days_in_house=25)

print(john.pays(bill=bill))
