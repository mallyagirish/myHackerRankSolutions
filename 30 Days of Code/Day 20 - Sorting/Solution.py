"""
@author: zepman85
"""

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

totalNumSwaps = 0
for i in range(n):
    numSwapsForThisIter = 0
    for j in range(n-1):
        if (a[j]>a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
            numSwapsForThisIter += 1
    
    totalNumSwaps += numSwapsForThisIter

    if numSwapsForThisIter == 0:
        break

print(f'Array is sorted in {totalNumSwaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[n-1]}')