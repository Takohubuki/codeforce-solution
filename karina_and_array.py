t = int(input())

test_cases = []

for _ in range(t):
    n = int(input())
    a = [int(item) for item in input().split(' ')]
    test_cases.append([n, a])

def solution(n: int, a: list) -> int:
    max_product = 0

    # 暴力破解
    # for i in range(len(a)):
    #     for j in range(len(a)):
    #         if i == j:
    #             continue
    #         max_product = max(a[i] * a[j], max_product)

    # 
    a.sort()
    max_product = max(a[0] * a[1], a[-1] * a[-2])
    return max_product
    
for test_case in test_cases:
    n = test_case[0]
    a = test_case[1]

    print(solution(n, a))
