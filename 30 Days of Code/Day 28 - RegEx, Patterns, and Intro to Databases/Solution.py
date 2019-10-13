"""
@author: zepman85
"""

import re

if __name__ == '__main__':
    N = int(input())

    firstNames = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        x = re.search("@gmail.com$",emailID)
        if x:
            firstNames.append(firstName)

    firstNames.sort()

    for name in firstNames:
        print(name)
