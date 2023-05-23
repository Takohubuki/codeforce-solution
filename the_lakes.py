t = int(input())

test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    print(a)