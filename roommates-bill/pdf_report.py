from fileinput import filename
import os
import webbrowser
from fpdf import FPDF
from bill import Bill
from roommate import Roommate

class PdfReport:
    """
    Creates a PDF file that contains data about the 
    roommates such as their names, amount owed, and 
    the billing period.
    """

    def __init__(self, filename) -> None:
        self.filename = filename

    def generate(self, roommate1: Roommate, roommate2: Roommate, bill: Bill):
        
        roommate1_pay = str(round(roommate1.pays(bill, roommate2), 2))
        roommate2_pay = str(round(roommate2.pays(bill, roommate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("/Users/jroumeliotis/oop-practice/roommates-bill/house.png", w=30, h=30)

        # Insert the title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Roommates Bill', border=0, align='C', ln=1)
        
        # Insert the Period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
        
        # Insert the name and amount due for the first roommate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=roommate1.name, border=0)
        pdf.cell(w=150, h=25, txt=roommate1_pay, border=0, ln=1)

        # Insert the name and amount due for the second roommate
        pdf.cell(w=100, h=25, txt=roommate2.name, border=0)
        pdf.cell(w=150, h=25, txt=roommate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open("file://" + os.path.realpath(self.filename))