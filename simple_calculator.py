a = float(input("enter first number: "))
b = float(input("enter second number: "))

oper = input("enter operation(+,-,*,/): ")

if oper =="+":
    print("result:", a + b)

elif oper == "-":
    print("result:", a - b)

elif oper == "*":
    print("result:", a * b)

elif oper == "/":
    if b != 0:
        print("result:", a / b)
    else:
        print("cannot divide by zero")

else:
    print("invalid operation")
