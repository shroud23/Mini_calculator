#lets build a calculator
a=int(input("enter your first number "))
operator=input("enter your operator (+ - * /)")
b=int(input("enter your second number"))
if operator=='+':
    c=a+b
    print(c)
elif operator=='-':
    c=a-b
    print(c)
elif operator=='*':
    c=a*b
    print(c)
else:
    c=a/b
    print(c)

