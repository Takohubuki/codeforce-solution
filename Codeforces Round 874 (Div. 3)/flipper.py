t = int(input())

test_cases = []

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    test_cases.append([n, p])

for case in test_cases:
    n, p = case