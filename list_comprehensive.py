#first way to create list
l=[]
for i in range(1,101):
    l.append(i)
print(l)
#second way to create list
n=[m for m in range(1,101)]
print(n)
# and how to apply filtration
n=[m for m in range(1,101) if m%2==0]
print(n)

j="jazib"
d=[q for q in j]
print(d)

j=[23,20,21,24,26]
n=[i for i in j if i%2==0]
print(n)
n[0] +=10
print(n)



