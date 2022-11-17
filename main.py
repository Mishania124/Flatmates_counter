from fpdf import FPDF
import webbrowser


class Bill:
    """
    Object that contains data about a bill such as
    total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def gererate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image(name="R.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=100, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=100, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)


a = int(input('Hey user,enter bill amount: '))
b = input('Enter the period: ')
c = input('Enter the first name of flatmate: ')
d = int(input('Enter how much days first flatmate was at home: '))
e = input('Enter the second name of flatmate: ')
f = int(input('Enter how much days second flatmate was at home: '))

the_bill = Bill(amount=a, period=b)
John = Flatmate(name=c, days_in_house=d)
Marry = Flatmate(name=e, days_in_house=f)
print(f'{c} pays:', round(John.pays(bill=the_bill, flatmate2=Marry),2))
print(f'{e} pays:', round(Marry.pays(bill=the_bill, flatmate2=John),2))

pdf_report = PdfReport(filename='Report1.pdf')
pdf_report.gererate(flatmate1=John, flatmate2=Marry, bill=the_bill)
