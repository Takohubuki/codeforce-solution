# AC
t = int(input())

test_cases = []

for _ in range(t):
    n = int(input())
    test_cases.append(n)

for case in test_cases:
    n = case
    s = 0
    while n:
        s += n
        n //= 2
    print(s)