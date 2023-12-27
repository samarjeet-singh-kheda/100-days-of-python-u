#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

bill_amt = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? (10, 12 or 15) ")
people = input("How many people would like to split the bill? ")

tip = float(bill_amt) * float(tip_percent) / 100
split = ( float(bill_amt) + float(tip) ) / int(people)

print(f"Each person should pay: ${round(split, 2)}")