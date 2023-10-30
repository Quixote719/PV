def Narcissistic():
    number = 100; res = []
    while number <= 999:
        d3 = number // 100
        d2 = number // 10 - d3 * 10
        d1 = number % 10
        if d3**3 + d2**3 + d1**3 == number: 
            res.append(number)
        number = number + 1
    return res

Q3 = Narcissistic()
print(Q3, len(Q3))