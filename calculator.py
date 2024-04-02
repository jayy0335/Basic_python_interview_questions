print("""
+ Addtion
- Subtraction
/ Division
* Multiply
""")

num1=eval(input("Enter your 1st Value:"))
num2= eval(input("Enter your 2nd valur:"))
opr=input("Enter your Operator..")

if opr == "+":
    print(num1+num2)
elif opr == "-":
    print(num1-num2)
elif opr == "/":
    print(num1/num2)
elif opr == "*":
    print(num1*num2)
else:
    print("Invalid Opr")
