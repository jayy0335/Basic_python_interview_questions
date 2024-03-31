# Question 8: Write a Python program to sort a list of elements using the bubble sort algorithm.

def bubble_sort(element):
    n=len(element)
    for i in range(n-1):
        for j in range (n-i-1):
            if element[j] > element [j + 1]:
                element[j] , element [j + 1] = element [j + 1] ,element[j]

# l=[5, 2, 8, 1, 9]
# find=bubble_sort(l)  
# print(find)
# ye none show kar raha q k ye variable me ha jabke humne return nahi karaya hai function me 
# without variable ye work karega

l=[5, 2, 8, 1, 9]
bubble_sort(l)  
print(l)

