t = int(input())

test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append([n, a])

for case in test_cases:
    n, a = case
    s = set()
    for x in a:
        s.add(x)
    if len(s) == 1:
        print(0)
        continue
    a.sort()
    cost = 0
    for i in range(n//2):
        cost += a[n - 1 - i] - a[i]
    print(cost)