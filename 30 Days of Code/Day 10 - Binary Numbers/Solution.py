"""
@author: zepman85
"""

if __name__ == '__main__':
    n = int(input())

    prevMaxVal = 0
    currMaxVal = 0
    val = n

    while val != 0:
        lastbit = val & 1

        if lastbit == 1:
            currMaxVal += 1
        else:
            if currMaxVal > prevMaxVal:
                prevMaxVal = currMaxVal
            currMaxVal = 0

        val = val >> 1

    if prevMaxVal > currMaxVal:
        currMaxVal = prevMaxVal

    print(currMaxVal)