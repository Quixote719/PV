# 1,2,3,4 could form how many 3-digit numbers with different digit
numArr = [1,2,3,4]

def Q1(arr, length):
    def numToStr(num):
        return str(num)
    
    strArr = list(map(numToStr, arr))

    def helper(curArr, targetLen):
        if(targetLen == length):
            return curArr
        updateArr = []
        for digit in strArr:
            for str in curArr:
                if str.find(digit) == -1:
                    updateArr.append(str + digit)
        return helper(updateArr, targetLen+1)
    
    return list(set(helper([''], 0)))

Q1ans = Q1(numArr, 3)
    
print(Q1ans, len(Q1ans))