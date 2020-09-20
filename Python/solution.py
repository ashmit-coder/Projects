# cook your dish here
lst = []
for i in range(int(input())):
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for j in P:
        if K % j == 0:
            lst.append(K // j)
    if len(lst) > 0:
        print(K // min(lst))
    else:
        print(-1)
    lst.clear()