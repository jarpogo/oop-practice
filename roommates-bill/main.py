import bill
import roommate
import pdf_report

the_bill = bill.Bill(amount=120, period="July 2022")
john = roommate.Roommate(name="John", days_in_house=20)
jane = roommate.Roommate(name="Jane", days_in_house=25)

print(f'John pays: {john.pays(bill=the_bill, roommate2=jane)}')
print(f'Jane pays: {jane.pays(bill=the_bill, roommate2=john)}')