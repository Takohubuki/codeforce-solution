from math import inf, isinf
t = int(input())

test_cases = []

for _ in range(t):
    n = int(input())
    book_list = []
    for _ in range(n):
        line = input().split()
        m = int(line[0])
        b_s = line[1]
        book_list.append((m, b_s))
    test_cases.append((n, book_list))

for case in test_cases:
    book_num = case[0]
    book_list = case[1]
    a_1, a_2 = [], []
    min_num = inf
    for idx, book_info in enumerate(book_list):
        if book_info[1] == '01':
            a_1.append(book_info[0])
        if book_info[1] == '10':
            a_2.append(book_info[0])
        if book_info[1] == '11':
            min_num = min(min_num, book_info[0])
    a_1.sort()
    a_2.sort()
    if len(a_1) > 0 and len(a_2) > 0:
        min_num = min(a_1[0] + a_2[0], min_num)
    if isinf(min_num):
        min_num = -1

    print(min_num)