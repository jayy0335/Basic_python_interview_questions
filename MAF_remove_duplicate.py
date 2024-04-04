# Question 10: Write a Python program to remove duplicates from a list.

def remove_deplicate(string):
    unique=[]
    for i in string:
        if i not in unique:
            unique.append(i)
    return unique 

c=[1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
f=remove_deplicate(c)
print(f)    
