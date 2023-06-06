def calculate_gas_cost(mileage, cost):
    distances = [20, 75, 500]
    costs = []

    for distance in distances:
        cost_for_distance = (distance / mileage) * cost
        costs.append(cost_for_distance)

    return costs

mileage = float(input())
cost = float(input())

calculated_costs = calculate_gas_cost(mileage, cost)
print(f'{calculated_costs[0]:.2f} {calculated_costs[1]:.2f} {calculated_costs[2]:.2f}')
