# Filename: P1HW2_morales stefan.py

# A travel expense calculator
# Date: 2023-06-02
# CTI-110 P1HW2 - Travel Expense
# Morales Stefan

def get_user_input():
    budget = float(input("Enter your budget in dollars (for example, 1500.00): "))
    destination = input("Enter your travel destination (for example, Paris): ")
    gas = float(input("Enter the estimated amount you will spend on gas in dollars (for example, 200.00): "))
    accommodation = float(input("Enter the estimated cost for accommodation/hotel in dollars (for example, 500.00): "))
    food = float(input("Lastly, enter the estimated amount you will need for food in dollars (for example, 300.00): "))
    return budget, destination, gas, accommodation, food

def calculate_expenses(gas, accommodation, food):
    return gas + accommodation + food

def calculate_remaining_budget(budget, expenses):
    return budget - expenses

def display_results(destination, budget, expenses, gas, accommodation, food, remaining_budget):
    print("------------Travel Expenses-----------")
    print(f"Location: {destination}")
    print(f"Initial Budget: ${budget:.2f}")
    print("\nExpenses:")
    print(f"Fuel: ${gas:.2f}")
    print(f"Accommodation: ${accommodation:.2f}")
    print(f"Food: ${food:.2f}")
    print(f"\nRemaining Balance: ${remaining_budget:.2f}")

def main():
    budget, destination, gas, accommodation, food = get_user_input()
    expenses = calculate_expenses(gas, accommodation, food)
    remaining_budget = calculate_remaining_budget(budget, expenses)
    display_results(destination, budget, expenses, gas, accommodation, food, remaining_budget)

if __name__ == "__main__":
    main()
