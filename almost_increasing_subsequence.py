n, q = map(int, input().split(' '))
a = input().split(' ')
for i, item in enumerate(a):
    a[i] = int(item)

queries = []
for i in range(q):
    queries.append([int(n) - 1 for n in input().split(' ')])

for start, end in queries:
    sub_seq = a[start:end+1]
    sub_len = len(sub_seq)
    sub_start, sub_end = 0, sub_len
    max_len = 0

    for i in range(sub_len):
        if i > 1 and sub_seq[i] <= sub_seq[i-1] and sub_seq[i-1] <= sub_seq[i-2]:
            temp_len = i - sub_start
            sub_start = i
            max_len = max(temp_len, max_len)
            
    if max_len == 0:
        max_len = sub_end - sub_start
    print(max_len)