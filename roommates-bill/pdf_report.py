import fpdf

class PdfReport:
    """
    Creates a PDF file that contains data about the 
    roommates such as their names, amount owed, and 
    the billing period.
    """

    def __init__(self, filename) -> None:
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        pass