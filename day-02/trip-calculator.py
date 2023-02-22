print("Welcome to the trip calculator.")
totalbill=input("What was the total bill?")
tip_percentage=input("What percentage tip would you like to give? 10, 12, or 15?")
noofpeople=input("How many people to split the bill?")

tip=int(totalbill)*(1+int(tip_percentage)/100)
bill_per_person=tip/int(noofpeople)
print(f"Each person should pay: {round(bill_per_person,2)}")