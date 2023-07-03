#Write a python program to calculate the ticket price in a theater based on the age of the customer.
#0-5 years=free
#6-12years=500
#13-17years=1000
#18+years=1500

age = int(input("Enter Customer's Age"))
if age >0 and age<=5:
    print("Free Entry!")
if age >6 and age<=12:
    print("Ticket costs 500")
if age >13 and age <=17:
    print("Ticket costs 1000")
else:
    print("Ticket costs 1500")
