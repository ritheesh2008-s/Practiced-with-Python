# Program: Check whether a number is prime using a function
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is prime")
else:
    print(num, "is not prime")
