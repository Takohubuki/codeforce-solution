def solution(n: int) -> int:
    total_len = n * 4
    total_len += n - 1
    i = 2
    # while i < n - 1:
    #     total_len += (n - i) * 2
    #     i += 1
    temp = (2 + (n - 2)) * (n - 3) 
    total_len += temp
    total_len += 3

    return total_len

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    test_cases.append(n)

for c in test_cases:
    print(solution(c))