# Program: Find the sum, largest and smallest number in a list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Sum      =", sum(numbers))
print("Largest  =", max(numbers))
print("Smallest =", min(numbers))
