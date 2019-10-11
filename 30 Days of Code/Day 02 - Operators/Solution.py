"""
@author: zepman85
"""

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    total_cost = meal_cost + tip_percent * meal_cost / 100.0 + tax_percent * meal_cost / 100.0

    total_cost = round(total_cost)
    print(total_cost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)