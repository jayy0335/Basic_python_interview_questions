def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest=largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

  
# test the function

c=[100,111,113,140,400,600]
d=find_second_largest(c)
print(d)

