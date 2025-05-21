print("Welcome to the tip calculator!")
totalBill = float(input("What was the total Bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
numberOfPeople = int(input("How many people to split the bill? "))
tipAsPercent = totalBill * (tip / 100)
billWithTip = totalBill + tipAsPercent
eachPersonsTip = round(billWithTip / numberOfPeople, 2)
print(f"Each person's tip is: ${eachPersonsTip}")
# eachTip = round((totalBill + (totalBill * tip)) / numberOfPeople, 2)

# print(f"Each person should pay: ${eachTip}" )
