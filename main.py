from flat import Bill, Flatmate
from reports import PdfReport

a = int(input('Hey user,enter bill amount: '))
b = input('Enter the period: ')

c = input('Enter the first name of flatmate: ')
d = int(input('Enter how much days first flatmate was at home: '))

e = input('Enter the second name of flatmate: ')
f = int(input('Enter how much days second flatmate was at home: '))

the_bill = Bill(amount=a, period=b)
John = Flatmate(name=c, days_in_house=d)
Marry = Flatmate(name=e, days_in_house=f)
print(f'{c} pays:', round(John.pays(bill=the_bill, flatmate2=Marry), 2))
print(f'{e} pays:', round(Marry.pays(bill=the_bill, flatmate2=John), 2))

pdf_report = PdfReport(filename='Report1.pdf')
pdf_report.gererate(flatmate1=John, flatmate2=Marry, bill=the_bill)
