N = int(input())
A = list(map(int, input().split()))
A_dic = { x: 0 for x in set(A)}
for a in A:
    A_dic[a] += 1
res_norm = sum([x*(x-1)//2 for x in A_dic.values()])
for a in A:
    print(res_norm - A_dic[a] + 1)