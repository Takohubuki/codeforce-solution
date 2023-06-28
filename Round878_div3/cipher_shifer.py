t = int(input())

test_cases = []

for _ in range(t):
    n = int(input())
    s = input()
    test_cases.append([n, s])

for case in test_cases:
    n, s = case
    a = ''
    temp = s[0]
    left, right = 0, 1
    while right < n:
        if s[left] == s[right]:
            a += s[left]
            left = right + 1
            right += 1
        right += 1
    print(a)
