"""
@author: zepman85
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

actualday, actualmonth, actualyear = map(int, input().rstrip().split())
expday, expmonth, expyear = map(int, input().rstrip().split())

if actualyear < expyear \
or (actualyear == expyear and actualmonth < expmonth) \
or (actualyear == expyear and actualmonth == expmonth and actualday <= expday):
    fine = 0

elif actualyear > expyear:
    fine = 10000
elif actualmonth == expmonth and actualday > expday:
    fine = 15 * (actualday - expday)
elif actualmonth > expmonth:
    fine = 500 * (actualmonth - expmonth)

print(fine)