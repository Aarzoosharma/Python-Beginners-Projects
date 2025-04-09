print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


#Calculate the tips
tip=bill*(tip/100)

#Calculate amount one person would pay
one_person= round((bill+tip)//people)

#print the split amount
print("Each person should pay: ",one_person)