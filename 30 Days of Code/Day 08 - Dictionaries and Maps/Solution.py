"""
@author: zepman85
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())

    phoneBook = {}
    for i in range(n):
        name,num = input().rstrip().split()
        phoneBook[name] = int(num)

    namesToLookup = []
    while True:
        try:
            name = input()
        except EOFError:
            break
        namesToLookup.append(name)

    for name in namesToLookup:
        if name in phoneBook:
            print(name+'='+str(phoneBook[name]))
        else:
            print('Not found')
