q = int(input())

cases = []
for _ in range(q):
    n, t = map(int, input().split(' '))
    v_t = [int(item) for item in input().split(' ')]
    v_e = [int(item) for item in input().split(' ')]
    cases.append([[n, t], v_t, v_e])

def solution(n: int, t: int, v_t: list, v_e: list) -> int:
    target = -1
    max_e = 0
    for i in range(n):
        if t - v_t[i] and v_e[i] > max_e:
            max_e = v_e[i]
            target = i
        t -= 1
        
    return target

for c in cases:
    n, t = c[0]
    v_t = c[1]
    v_e = c[2]
    print(solution(n, t, v_t, v_e))