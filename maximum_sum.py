# wrong on test 1
# 6 2
# 15 22 12 10 13 11
# --------------------
# updated ac
t = int(input())

test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    arr = [int(num) for num in input().split()]
    test_cases.append([n, k, arr])

for case in test_cases:
    n, k, arr = case
    arr.sort()
    # pre_sum = [sum(arr[:i]) for i in range(1, len(arr) + 1)]
    pre_sum = [0] * (n+1)
    for i in range(n):
        pre_sum[i+1] = pre_sum[i] + arr[i]

    # while k > 0:
    #     if pre_sum[-2] > pre_sum[-1] - pre_sum[1]:
    #         pre_sum = pre_sum[:-1]
    #     else:
    #         temp = pre_sum[1]
    #         pre_sum = pre_sum[2:]
    #         pre_sum = list(map(lambda a: a-temp, pre_sum))
    #     k -= 1
    # print(pre_sum[-1])
    ans = 0
    for i in range(k+1):
        ans = max(ans, pre_sum[n - k + i] - pre_sum[2 * i])
    print(ans)