# Question 5: Write a Python program to count the frequency of each element in a list.

def count_frequency(numbers):
    frequency={}
    for i in numbers:
        if i in frequency:
            frequency[i] +=1
        else:
            frequency[i]=1
    return frequency

k=[22,21,12,1,2,12,1,234,456,65,34,5345,345,45,35,345,345]
l=count_frequency(k)
print(l)

for j in l.items():
    print(j)