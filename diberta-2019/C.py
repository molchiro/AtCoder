N = int(input())

innerAB_cnt = 0
endA_cnt = 0
startB_cnt = 0
B_A_cnt = 0
for i in range(N):
    S = input()
    innerAB_cnt += S.count('AB')
    is_end_A = S[-1] == 'A'
    is_start_B = S[0] == 'B'
    if is_end_A and is_start_B:
        B_A_cnt += 1
    elif is_end_A:
        endA_cnt += 1
    elif is_start_B:
        startB_cnt += 1
remainder = abs(startB_cnt - endA_cnt)
if B_A_cnt == 0:
    print(min(endA_cnt, startB_cnt) + innerAB_cnt)
elif endA_cnt + startB_cnt > 0:
    print(min(endA_cnt, startB_cnt) + B_A_cnt + innerAB_cnt)
else:
    print(B_A_cnt-1 + innerAB_cnt)


