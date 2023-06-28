t = int(input())

test_cases = []

for _ in range(t):
    n = int(input())
    tree = []
    for _ in range(n-1):
        tree.append(list(map(int, input().split())))

    q = int(input())
    vertices = []
    for _ in range(q):
        vertices.append(list(map(int, input().split())))
    
    test_cases.append([n, tree, q, vertices])

# find the position of verices pair (x, y) in the binary tree, and find the leaf vertix of this sub tree
for case in test_cases:
    n, tree, q, vertices = case
    adj = [[] for _ in range(n)]
    cnt = [0] * n
    for u, v in tree:
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    def dfs(root, fa):
        if len(adj[root]) == 1 and adj[root][0] == fa:
            cnt[root] = 1
        else:
            for u in adj[root]:
                if u != fa:
                    dfs(u, root)
                    cnt[root] += cnt[u]
    
    dfs(0, -1)
    for c, k in vertices:
        c -= 1
        k -= 1
        print(cnt[c] * cnt[k])