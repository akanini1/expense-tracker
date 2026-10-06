# Expense Tracker - Installment 3: The Tracker Does Math 
# Author: Prince Diether M. Sampang
# Adds subtotal, tax, grand total, and budget calculations.

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0 

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * tax_percent / 100
total = subtotal + tax
over_budget = total > budget
left = budget - total


print()
print("-" * 40)
print("SUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)
print("Made by: Prince Diether M. Sampang | Installment 3")