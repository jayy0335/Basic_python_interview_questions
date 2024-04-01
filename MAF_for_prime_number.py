# Question 6: Write a Python program to check if a number is prime.

def is_prime(number):
    if number <2:
        return False
    for i in range (2, int (number ** 0.5) +1):
        if  number % i == 0:
            return False
    return True

check=19
if is_prime(check):
    print(f"{check} is a prime number")
else:
    print(f"{check} is not a prime number")

print(check**0.5)
print(int(check**0.5))
print(int(check**0.5) +1)