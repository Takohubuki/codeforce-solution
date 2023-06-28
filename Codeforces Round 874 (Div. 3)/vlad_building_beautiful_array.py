t = int(input())

test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append([n, a])

for case in test_cases:
    n, a = case