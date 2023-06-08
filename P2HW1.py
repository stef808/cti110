# Filename: P2HW1_morales stefan.py
# A travel expense calculator
# Date: 2023-06-7
# CTI-110 P2Hw1 - Travel Expense
# Morales Stefan

def get_user_input():
    budget = float(input("Enter budget: "))
    destination = input("Enter your travel destination: ")
    gas = float(input("How much do you think you will spend on gas: "))
    accommodation = float(input("Approximnately, how much will you need for accomodation/hotel?: "))
    food = float(input("Last, how much will you need for food: "))
    return budget, destination, gas, accommodation, food

def calculate_expenses(gas, accommodation, food):
    return gas + accommodation + food

def calculate_remaining_budget(budget, expenses):
    return budget - expenses

def display_results(destination, budget, expenses, gas, accommodation, food, remaining_budget):
    print("------------Travel Expenses-----------")
    print("Location:", destination)
    print("Initial Budget: $%.2f" % budget)
    print("\nExpenses:")
    print("Fuel: $%.2f" % gas)
    print("Accommodation: $%.2f" % accommodation)
    print("Food: $%.2f" % food)
    print("--------------------------------------")
    print("Remaining Balance: $%.2f" % remaining_budget)

def main():
    budget, destination, gas, accommodation, food = get_user_input()
    expenses = calculate_expenses(gas, accommodation, food)
    remaining_budget = calculate_remaining_budget(budget, expenses)
    display_results(destination, budget, expenses, gas, accommodation, food, remaining_budget)

if __name__ == "__main__":
    main()
