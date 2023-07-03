#create a python program to check if a given year is leap
#The year is divisible by 4 but not divisible by 100
#except if its also divisible by 400

year = int(input("Enter Year Number"))
if(year % 4 == 0) or (year % 100 != 0) and (year % 400 == 0):
    print("Is A leap Year")
else:
    print("Not A leap Year")
