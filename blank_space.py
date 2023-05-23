# wrong on test2
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    test_cases.append((n, arr))

for case in test_cases:
    arr_len = case[0]
    arr = case[1]
    max_blank = 0
    zero_cnt = 0
    for num in arr:
        if num == 0:
            zero_cnt += 1
        else:
            max_blank = max(max_blank, zero_cnt)
            zero_cnt = 0
    max_blank = max(max_blank, zero_cnt)

    print(max_blank)