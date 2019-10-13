"""
@author: zepman85
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
if __name__ == '__main__':
    n = int(input())

    numbers = []
    for i in range(n):
        numbers.append(int(input()))

    for number in numbers:
        if number == 1 \
        or (number > 2 and (number % 2 == 0)) \
        or (number > 3 and (number % 3 == 0)) \
        or (number > 5 and (number % 10 not in [1,3,7,9])) \
        or (number > 9 and (number % 10 in [0,5])):
            print('Not prime')
            continue
    
        for i in range(5, math.ceil(math.sqrt(number))+1):
            if number % i == 0:
                print('Not prime')
                break
        else:
            print('Prime')
