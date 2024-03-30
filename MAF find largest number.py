# Question 3: Write a Python program to find the largest element in a list.

def find_large(number):
    largest=number[0]
    for i in number:
        if i>largest:
            largest=i
    return largest

l=[22,33,44,55,66,77]
f=find_large(l)
print(f"{f} is the largest number")

print("Smallest function below")

def smallest_number(number):
    smallest=number[0]
    for i in number:
        if i < smallest:
            smallest=i
    return  smallest

c=[222,331,212,313,4534,656,776]
check=smallest_number(c)
print(f"{check} is the smallest value in c")