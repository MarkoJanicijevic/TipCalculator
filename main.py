print("Welcome to the tip calculator!")
bill = int(input("What is your total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10%, 12% or 15% "))
number_of_people = int(input("How many people to split the bill? "))
result = round(((bill * (1 + tip_percentage / 100)) / number_of_people), 2);
print(f"Each person has to pay {result}")
