"""
@author: zepman85
"""

T = int(input())

S = []
for i in range(T):
    S.append(input())

for s in S:
  print(s[0::2],s[1::2])