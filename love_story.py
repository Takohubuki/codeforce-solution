# ac
t = int(input())
s = []
for _ in range(t):
    s.append(input())

res = []
target = 'codeforces'

for ss in s:
    cnt = 0
    for i in range(len(target)):
        if target[i] != ss[i]:
            cnt += 1
    res.append(cnt)

for item in res:
    print(item)