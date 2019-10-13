"""
@author: zepman85
"""

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

import math
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        if n == 1:
            return 1

        sumOfDivisors = 1 + n
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                sumOfDivisors += i
                d = int(n/i)
                if d != i:
                    sumOfDivisors += d
        
        return sumOfDivisors

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)