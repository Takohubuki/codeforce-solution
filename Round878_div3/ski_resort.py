# memory out of limit on test3
# ac
t = int(input())

test_cases = []

for _ in range(t):
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append([n, k, q, a])

# n: len of target seq
# m: len of sub seq
# def arrangeSeq(n, m):
#     ans = 0
#     if m > n:
#         return ans
#     for i in range(m, n):
#         ans += (n - i + 1)
#     return ans + 1

for case in test_cases:
    n, k, q, a = case
    ans = 0
    len = 0
    for i in range(n):
        if a[i] <= q:
            len += 1
        else:
            if len >= k:
                ans += (len - k + 1) * (len - k + 2) // 2
            len = 0
    if len >= k:
        ans += (len - k + 1) * (len - k + 2) // 2
    # dp
    # def dfs(t):
    #     if len(t) < k or all(x > q for x in t):
    #         return 0
    #     elif len(t) == k and all(x <= q for x in t):
    #         return 1
    #     if all(x <= q for x in t):
    #         return arrangeSeq(len(t), k)
    #     for i, x in enumerate(t):
    #         if x > q:
    #             return dfs(t[:i]) + dfs(t[i+1:])
    # ans = dfs(a)
    print(ans)
