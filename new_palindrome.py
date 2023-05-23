# ac
from collections import Counter
t = int(input())

test_cases = []

for _ in range(t):
    test_cases.append(input())

# aaacaaa
for case in test_cases:
    counter = Counter(case)
    if len(counter.keys()) > 2:
        print('yes')
        continue
    n = len(case)
    prefix = case[:n//2]
    # abaaba => aabbaa
    sub_cnter = Counter(prefix)
    if len(sub_cnter) == 2:
        print('yes')
    else:
        print('no')