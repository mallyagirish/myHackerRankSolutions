"""
@author: zepman85
"""

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    
    def computeDifference(self):
        maxVal = max(self.__elements)
        minVal = min(self.__elements)
        self.maximumDifference = maxVal-minVal

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)