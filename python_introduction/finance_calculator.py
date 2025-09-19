income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
print (f"Your monthly savings are ${income - expenses}.")
print (f"Projected savings after one year, with interest, is: ${int((income * 12) + (income * 12 * 0.05))}.")
