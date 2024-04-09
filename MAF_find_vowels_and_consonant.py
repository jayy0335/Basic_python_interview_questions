user_input = input("enter your sentance:-")

v=0
c=0

for i in user_input:
    if i in ["a","e","i","o","u"]:
        v=v+1
    elif i==" ":
        pass
    else:
        c=c+1

print(f" the number of vowels in user's input is {v}")
print(f" the number the consonants in user's input is {c}")
