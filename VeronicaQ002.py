num1 = 24; num2 = 15

def LCM(num1, num2):
    maxNum = max(num1, num2); minNum = min(num1, num2); index = 2; res = maxNum
    while(res % minNum != 0):
        res = index * maxNum
        index = index + 1
    return res

print(LCM(num1, num2))