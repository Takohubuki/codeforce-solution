t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(num) for num in input().split()]

    # a_contrast = sum(arr[i] - arr[i+1] for i in range(n-1))
    len_b = 0
    a_contrast = [abs(arr[i] - arr[i+1]) for i in range(n-1)]
    pre_sum_a_contrast = [sum(a_contrast[:i]) for i in range(len(a_contrast)+1)]

    for i in range(len(pre_sum_a_contrast)-1):
        if pre_sum_a_contrast[i] != pre_sum_a_contrast[i+1]:
            len_b += 1

    print(len_b)