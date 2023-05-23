# 经典的递归/dp
# ac
from functools import cache

t = int(input())

test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    test_cases.append((n, m))

@cache
def divideGold(start, target) -> bool:
    if target > start and start % 3:
        return False
    if start/3 == target or start*2 / 3 == target:
        return True
    
    p1 = divideGold(start*2/3, target)
    p2 = divideGold(start/3, target)

    return p1 or p2

for case in test_cases:
    start, target = case
    if target > start:
        print('no')
        continue
    elif target == start:
        print('yes')
        continue

    if divideGold(start, target):
        print('yes')
    else:
        print('no')