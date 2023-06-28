t = int(input())

test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append([n, a])

for case in test_cases:
    n, a = case
    if n <= 3:
        print(0)
        continue
    s = set()
    for x in a:
        s.add(x)
    if len(s) == 3:
        print(0)
        continue
