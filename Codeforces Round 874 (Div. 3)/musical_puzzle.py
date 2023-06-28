# ac
t = int(input())

test_cases = []

for _ in range(t):
    n = int(input())
    s = input()
    test_cases.append([n, s])

for case in test_cases:
    n, s = case
    m_set = set()
    for i in range(n-1):
        if s[i:i+2] not in m_set:
            m_set.add(s[i:i+2])
    print(len(m_set))