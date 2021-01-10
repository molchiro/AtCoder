from bisect import bisect_right

N, Q = list(map(int, input().split()))

row_list = [-N+1]
col_list = [-N+1]
row_dic = {N-1: N-2}
col_dic = {N-1: N-2}
row_min = N-1
col_min = N-1

ans = (N-2)**2
for _ in range(Q):
    q, x = input().split()
    x = int(x)-1
    if q == '1':
        index = bisect_right(row_list, -x)-1
        key = -row_list[index]
        val = row_dic[key]
        ans -= val
        if x < row_min:
            row_min = x
            if not col_min in col_dic:
                col_list.append(-col_min)
            col_dic[col_min] = x-1
    else:
        index = bisect_right(col_list, -x)-1
        key = -col_list[index]
        val = col_dic[key]
        ans -= val
        if x < col_min:
            col_min = x
            if not row_min in row_dic:
                row_list.append(-row_min)
            row_dic[row_min] = x-1
print(ans)
