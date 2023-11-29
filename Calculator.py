#Basic Calculator(Only For Integer Number)
first = input("enter first number :")
operator = input("enter operator(+,-,*,/,%):")
second = input("enter second number :")
first = int(first)
second = int(second)
if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator == "*":
    print(first*second)
elif operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
else:
    print("Invalid Operation")
#Better Calculator(With Decimal Numbers)
first = float(input("enter first number :"))
operator = input("enter operator(+,-,*,/,%):")
second = float(input("enter second number :"))
if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator == "*":
    print(first*second)
elif operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
else:
    print("Invalid Operation")