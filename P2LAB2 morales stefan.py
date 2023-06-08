num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# Compute their product and average
product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4

# Print product and average as integers (rounded)
print(f'{product:.0f} {average:.0f}')

# Print product and average as floating-point numbers
print(f'{product:.3f} {average:.3f}')