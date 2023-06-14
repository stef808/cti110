# Get input integer numbers from user
num1 = int(input())
num2 = int(input())

# Check if the value of num1 is less than or equal to the value of num2
if num1 <= num2:
    # Iterating while loop
    while num1 <= num2:
        # Print the value of num1
        print(num1, end=" ")
        # Value of num1 is incremented by 5
        num1 += 5
    # Print an end with a newline
    print()
else:
    # Otherwise display output
    print("Second integer can't be less than the first.")


