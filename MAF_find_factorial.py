# Question 2: Write a Python program to find the factorial of a number.


def factorial(n):
    if  n==0:
        return 1
    else:
        return n * factorial(n-1)


number=5
result=factorial(number)
print(f"factorial of {number} is {result}")

#
# for i in range (10):
#     print(factorial(i))