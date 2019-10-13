"""
@author: zepman85
"""

from operator import add

def hourglassSum(centreRowAndColInd, arr):
    # define offsets, for the hourglass shape, these are offsets to
    # top, and bottom rows (i.e., exclude middle row)
    # left, middle, and right cols
    rowOffsets = (-1, 1)
    colOffsets = (-1, 0, 1)
    # calculate sum of all elements of the shape using the offsets
    # init sum with centre val
    sum = arr[centreRowAndColInd[0]][centreRowAndColInd[1]]
    for i in rowOffsets:
        for j in colOffsets:
            ind = tuple(map(add, (i,j), centreRowAndColInd))
            sum += arr[ind[0]][ind[1]]
    
    return sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # list the centre coordinates of all possible hourglasses   
    y = list((i,j) for i in range(1,5) for j in range(1,5))

    # find the list of sums of all possible hourglasses
    sums = [hourglassSum(centreInd, arr) for centreInd in y]

    print(max(sums))
