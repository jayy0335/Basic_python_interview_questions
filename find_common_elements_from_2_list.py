# Question 7: Write a Python program to find the common elements between two lists.

def find_common(list1,list2):
    elements=[]
    for i in list1:
        if i in list2:
            elements.append(i)
    return elements


a=[1,2,3,4,5]
b=[4,5,6,7,8,9]
c=find_common(a,b)
print(c)

