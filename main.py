from flat import Bill, Flatmate
from reports import PDFReport

bill_amt = float(input("Enter the bill amount: "))
period = input("Enter the billing month: ")
flatmate1 = input("Enter name of flatmate1: ")
days_in_house_f1 = int(input(f"Enter number of days {flatmate1} is in house: "))
flatmate2 = input("Enter name of flatmate2: ")
days_in_house_f2 = int(input(f"Enter number of days {flatmate2} is in house: "))


bill: Bill = Bill(amt=bill_amt, period=period)
f1 = Flatmate(name=flatmate1, days_in_house=days_in_house_f1)
f2 = Flatmate(name=flatmate2, days_in_house=days_in_house_f2)

print(f"{f1.name} pays: ",f1.pays(bill,f2))
print(f"{f2.name} pays: ",f2.pays(bill,f1))

pdf = PDFReport(f"{period.replace(' ','_')}")
pdf.generate(f1,f2,bill)
