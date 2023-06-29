def mitmorn():
    print("This is MIT Morning class")


mitmorn()


def calculate():
    x = 7
    y = 10
    print(x * y)
    print(x + y)
    print(x - y)
    print(x / y)


calculate()


def majina(myfirstname, mylastname, Age):
    print("my name is", myfirstname + " " + mylastname + " " + "my age is", Age)


majina("Alex", "Theuri", 20)
majina("Emm", "Byhold", 19)
majina("John", "Snow", 16)
majina("Stacy", "Mula", 27)
majina("Erick", "Were", 24)


# function to calculate the average of a number

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total/ count
    return average

data = [3,6,8,9,2,1,8]
result = calculate_average(data)
print("The average is", result)

#create a function that will create a palandrome(the longest string)