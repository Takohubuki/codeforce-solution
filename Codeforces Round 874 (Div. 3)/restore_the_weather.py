t = int(input())

test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append([n, k, a, b])

for case in test_cases:
    n, k, a, b = case
    sorted_a = sorted(a)
    sort_indices = [i for i, x in sorted(enumerate(a), key=lambda pair: pair[1])]

    for i in range(n):
        print(b[sort_indices[i]])