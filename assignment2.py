def add(p, q):
    return p + q


def subtract(p, q):
    return p - q


def multiply(p, q):
    return p * q


def division(p, q):
    return p / q


print("Select Operation")
print("a. Addition")
print("b. subtraction")
print("c. multiply")
print("d. division")

choice = input("enter choice (a/b/c/d)\n")
num1 = int and float(input("please enter first number"))
num2 = int and float(input("please enter second number"))

if choice == 'a':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 'b':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 'c':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 'd':
    print(num1, "+", num2, "=", add(num1, num2))
else:
    print("invalid number")
