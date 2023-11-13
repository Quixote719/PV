def add(num1, num2):
    return num1 + num2

def addMulti(*arg):
    sum = 0
    for param in arg:
        sum += param
    return sum

print(add(2,5), add(3,6))

print(addMulti(3,4,5,6,7,8,9))